========================================
PROJECT TITLE: STUDENT SONG PORTAL
========================================

Author: Navid Hossain
Framework: Django (Python)
Theme: Green & White Tech Theme
Background Image: tech-pattern.png (static, fixed)
Chatbot: Integrated AI assistant for guidance

----------------------------------------
1. PROJECT OVERVIEW
----------------------------------------
The Student Song Portal is a Django web application designed for students to register,
check their application status, and access curated music in a safe, verified environment.
It provides a modern UI with a fixed background image, responsive forms, and an integrated
AI chatbot assistant.

Key features:
- Verified student access
- Admin panel with CRUD capabilities
- Status checking for applications
- Curated study-friendly music content
- AI chatbot guidance for portal navigation

----------------------------------------
2. FILE STRUCTURE
----------------------------------------
Project directory:

app1/                      <- Main Django project
├── __init__.py
├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py

MusicPortal/               <- Django application
├── __init__.py
├── models.py              <- StudentApplication model
├── forms.py               <- ApplicationForm
├── views.py               <- All views including chatbot
└── urls.py                <- App URLs

templates/
└── Music/
    ├── base.html           <- Main layout with navbar, footer, background
    ├── home.html           <- Homepage with hero section and chatbot
    ├── apply.html          <- Registration form
    ├── check_status.html   <- Student status checking page
    ├── admin_login.html    <- Admin login page
    └── admin_panel.html    <- Admin dashboard with CRUD actions

static/
└── app1/
    ├── style.css           <- Custom CSS for portal styling
    ├── tech-pattern.png    <- Background image
    └── cartoon.png         <- Chatbot placeholder image

----------------------------------------
3. MODELS (models.py)
----------------------------------------
StudentApplication:
- full_name (CharField)
- reg_no (CharField)
- university_name (CharField)
- district (CharField)
- age (IntegerField)
- guardian_name (CharField)
- address_city (CharField)
- address_district (CharField)
- address_state (CharField)
- certificate (FileField)
- status (CharField: Pending/Approved/Denied)
- remarks (TextField, optional)

----------------------------------------
4. FORMS (forms.py)
----------------------------------------
ApplicationForm:
- ModelForm based on StudentApplication
- Fields: full_name, reg_no, university_name, district, age, guardian_name, 
  address_city, address_district, address_state, certificate

----------------------------------------
5. VIEWS (views.py)
----------------------------------------
- home(request): Renders homepage with chatbot
- apply(request): Handles student registration form
- check_status(request): Students check application status by reg_no & university
- admin_login(request): Admin login verification
- admin_panel(request): Displays all student applications
- update_status(request, student_id, new_status): Updates student application status
- chatbot_response(request): AI chatbot response via OpenAI API

----------------------------------------
6. URLS (urls.py)
----------------------------------------
- '' → home
- 'apply/' → apply
- 'check_status/' → check_status
- 'admin_login/' → admin_login
- 'admin_panel/' → admin_panel
- 'update_status/<int:student_id>/<str:new_status>/' → update_status
- 'chatbot_response/' → chatbot_response

Include in app1/urls.py:
    path('MusicPortal/', include('MusicPortal.urls'))

----------------------------------------
7. USER INPUTS
----------------------------------------
- Registration Form: full_name, reg_no, university_name, district, age, guardian_name, 
  address_city, address_district, address_state, certificate upload
- Check Status: reg_no, university_name
- Admin Login: username, password
- Chatbot: user text input message

----------------------------------------
8. WORKING
----------------------------------------
1. Homepage displays portal overview, features, and chatbot.
2. Students submit applications via Apply page.
3. Status can be checked using Check Status page.
4. Admin logs in via Admin Login and manages applications in Admin Panel.
5. Admin can Approve or Deny applications; students are notified of status.
6. Chatbot answers queries regarding registration, status, portal usage, and music access.
7. Fixed background image remains visible while scrolling content.
8. Forms are semi-transparent to allow readability without hiding the background.

----------------------------------------
9. COMMANDS TO RUN
----------------------------------------
1. Create virtual environment:
    python -m venv venv
    venv\Scripts\activate   (Windows)
    source venv/bin/activate (Linux/Mac)

2. Install dependencies:
    pip install django openai

3. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

4. Create superuser (optional):
    python manage.py createsuperuser

5. Run development server:
    python manage.py runserver

6. Open browser:
    http://127.0.0.1:8000/MusicPortal/

----------------------------------------
10. NOTES
----------------------------------------
- Ensure static files are correctly referenced for CSS and images.
- Chatbot requires OpenAI API key configured in views.py.
- Uploaded certificates are stored in MEDIA_ROOT/uploads/; ensure MEDIA_URL & MEDIA_ROOT are configured in settings.py if needed.

----------------------------------------
END OF DOCUMENT
----------------------------------------
