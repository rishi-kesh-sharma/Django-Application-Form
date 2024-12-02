from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_application_form, name='employee_application_form'),  # Employee application form page
    path('success/', views.application_success, name='application_success'),  # Success page after submission
]
