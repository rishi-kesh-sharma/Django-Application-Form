from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_application_form, name='employee_application_form'),  # Employee application form page
    path('success/', views.application_success, name='application_success'),
    path('download/<id>/',views.download_pdf,name='download_pdf')  ,
    # url(r'^download/(\d+)/$', 'form.views.download_pdf', name='pdf_by_id'),
]
