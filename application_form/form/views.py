from django.shortcuts import render, redirect
from .forms import EmployeeApplicationForm
from django.template.loader import render_to_string
from form.models import Form
from django.template.loader import get_template
from xhtml2pdf import pisa



def employee_application_form(request):
    if request.method == "POST":
        form = EmployeeApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            saved_form=  form.save()
            # return redirect(request,'application_success',{"data":saved_form})
            return render(request, 'form_app/success.html',{"data":saved_form})

    else:
        form = EmployeeApplicationForm()
    return render(request, 'form_app/employee_application_form.html', {'form': form})

def application_success(request):
    return render(request, 'form_app/success.html')


def download_pdf(request,id):
    application_data = Form.objects.get(pk=id)
    rendered = render_to_string('form_app/application_form_filled.html',{'data':application_data})
    #  print(rendered)   
     # enable logging
    pisa.showLogging()
    pdf_path = "static/application_pdf/"+id+".pdf"
    with open(pdf_path, "w+b") as result_file:
    # convert HTML to PDF
     pisa_status = pisa.CreatePDF(
        rendered,       
        dest=result_file,  
    )
    # Check for errors
    if pisa_status.err:
     print("An error occurred!")                                         

    redirect_url="/static/application_pdf/"+id+".pdf/"
    return redirect(redirect_url)
    # return redirect(pdf_path)
    # return render(request, 'form_app/success.html')

    