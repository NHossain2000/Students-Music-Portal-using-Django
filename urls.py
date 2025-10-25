from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('check_status/', views.check_status, name='check_status'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('update_status/<int:student_id>/<str:new_status>/', views.update_status, name='update_status'),

    # ✅ Add this line for chatbot
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
]
