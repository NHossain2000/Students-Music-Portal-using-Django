from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from .forms import ApplicationForm
from .models import StudentApplication

# Initialize OpenAI client
client = OpenAI(api_key="Your API key")

# ----------------- Homepage -----------------
def home(request):
    return render(request, 'Music/home.html')

# ----------------- Student Apply Form -----------------
def apply(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'Music/apply.html', {'form': form})

# ----------------- Check Status -----------------
def check_status(request):
    status = None
    if request.method == 'POST':
        reg_no = request.POST.get('reg_no')
        university_name = request.POST.get('university_name')
        try:
            student = StudentApplication.objects.get(reg_no=reg_no, university_name=university_name)
            status = student.status
        except StudentApplication.DoesNotExist:
            status = "No record found."
    return render(request, 'Music/check_status.html', {'status': status})

# ----------------- Admin Login -----------------
def admin_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if user == 'admin' and pwd == 'admin123':
            return redirect('admin_panel')
    return render(request, 'Music/admin_login.html')

# ----------------- Admin Panel (CRUD) -----------------
def admin_panel(request):
    students = StudentApplication.objects.all()
    return render(request, 'Music/admin_panel.html', {'students': students})

def update_status(request, student_id, new_status):
    student = get_object_or_404(StudentApplication, id=student_id)
    student.status = new_status
    student.save()
    return redirect('admin_panel')

# ----------------- Chatbot -----------------
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')

        system_prompt = '''
        The Student Song Portal is a modern, student-focused website designed to provide verified students with curated music content that enhances focus, creativity, learning, and overall productivity. Unlike general music streaming portals, this platform ensures that only registered students with valid credentials can access its content, creating a safe, educational, and purpose-driven environment for music consumption.

        Advantages of the Student Song Portal over normal song portals include:
        1. **Verified Access**: Students must submit registration certificates and university details to gain access, ensuring a secure and exclusive community.
        2. **Focused Content**: The platform curates music tracks that are particularly beneficial for studying, concentration, and stress relief, rather than general entertainment.
        3. **Educational Integration**: By combining music access with task verification and student workflows, the portal helps students manage tasks efficiently while enjoying music.
        4. **Administrative Oversight**: Admin verification of submissions ensures quality control and prevents misuse or unauthorized access.
        5. **AI Assistance**: An integrated AI chatbot helps students navigate the portal, understand procedures, and get immediate answers to queries, which is not commonly available on normal music portals.

        The website layout consists of several pages, each serving a specific purpose:
        - **Homepage**: Introduces the Student Song Portal, highlights the importance of music in student life, explains available services, and provides access to the chatbot for instant assistance.
        - **Registration Form (Apply Page)**: Students provide personal details such as full name, age, guardian’s name, and address (city, district, state), as well as university-specific information including registration number, university name, and district. Students must also upload a registration certificate image or PDF.
        - **Check Status Page**: Students can input their registration number and university name to view whether their application is approved, denied, or pending verification, ensuring transparency.
        - **Admin Panel**: Admins log in to a secure dashboard where they can view all student applications, verify certificates, and perform CRUD operations including approving, denying, or leaving applications pending.
        - **Music Access Page**: Approved students can access sample curated music tracks embedded from sources like YouTube NCS. Denied students are notified of access denial, and pending applications are clearly marked.

        Benefits for students:
        - **Enhanced Focus and Productivity**: Access to curated study-friendly music that improves concentration.
        - **Safe and Exclusive Environment**: Only verified students can access content, reducing distractions and inappropriate content.
        - **Guided Workflow**: Students can easily track their application status and know the next steps, reducing confusion.
        - **AI Assistance**: Immediate answers from the chatbot guide students on registration, verification, content access, and general website navigation.

        The website also covers common questions and queries students may have:
        - How to apply and submit a registration certificate.
        - What documents are required for verification.
        - How to check application status.
        - What to do if access is pending or denied.
        - How to navigate the admin panel (for admins).
        - How to access sample music tracks after approval.

        Overall, the Student Song Portal modernizes task management related to student access to music resources by combining secure form submissions, administrative verification, curated content, and AI chatbot assistance. The portal is professionally designed with smooth navigation, consistent layout, responsive pages, and user-friendly interfaces. It is an interactive, educational, and beneficial environment for students, providing a unique advantage over standard music streaming portals by aligning music access with verified academic identity, learning enhancement, and productivity support.
        '''

        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = completion.choices[0].message.content.strip()
        except Exception as e:
            answer = f"Sorry, there was an error: {str(e)}"

        return JsonResponse({'reply': answer})

    return JsonResponse({'reply': 'Invalid request method'}, status=400)
