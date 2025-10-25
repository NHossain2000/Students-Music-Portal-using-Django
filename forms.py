from django import forms
from .models import StudentApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = [
            'full_name', 'reg_no', 'university_name', 'district',
            'age', 'guardian_name', 'address_city',
            'address_district', 'address_state', 'certificate'
        ]
