from django.db import models

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Denied', 'Denied'),
]

class StudentApplication(models.Model):
    full_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50)
    university_name = models.CharField(max_length=150)
    district = models.CharField(max_length=100)
    age = models.IntegerField()
    guardian_name = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_district = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    certificate = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.status}"
