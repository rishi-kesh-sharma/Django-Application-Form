from django.shortcuts import render, redirect
from .forms import EmployeeApplicationForm


def employee_application_form(request):
    if request.method == "POST":
        form = EmployeeApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('application_success')
    else:
        form = EmployeeApplicationForm()
    return render(request, 'form_app/employee_application_form.html', {'form': form})

def application_success(request):
    return render(request, 'form_app/success.html')
