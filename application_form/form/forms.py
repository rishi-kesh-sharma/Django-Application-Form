from django import forms
from .models import Form  # Assuming the Form model is being repurposed for employee applications

class EmployeeApplicationForm(forms.ModelForm):
    class Meta:
        model = Form  # Replace with Employee model if using a dedicated model
        fields = [
            'official_given_names', 
            'surnames', 
            'address', 
            'zip_code_and_place', 
            'email_address', 
            'telephone_number', 
            'date_of_birth', 
            'place_of_birth', 
            'bsn', 
            'iban_number', 
            'nationality', 
            'number_id', 
            'id_date_of_expiry', 
            'marital_status', 
            'name_spouse', 
            'travel_to_work', 
            'available_from_date', 
            'shirt_size', 
            'trouser_size', 
            'id_front', 
            'id_back', 
            'bank_card', 
            'health_insurance_front', 
            'health_insurance_back', 
            'work_permit'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'id_date_of_expiry': forms.DateInput(attrs={'type': 'date'}),
            'available_from_date': forms.DateInput(attrs={'type': 'date'}),
        }
