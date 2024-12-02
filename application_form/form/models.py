from django.db import models

class Form(models.Model):
    official_given_names = models.CharField(max_length=255, verbose_name="Official Given Names")
    surnames = models.CharField(max_length=255, verbose_name="Surnames")
    address = models.TextField(verbose_name="Address")
    zip_code_and_place = models.CharField(max_length=255, verbose_name="ZIP Code and Place")
    email_address = models.EmailField(verbose_name="Email Address")
    telephone_number = models.CharField(max_length=20, verbose_name="Telephone Number")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    place_of_birth = models.CharField(max_length=255, verbose_name="Place of Birth")
    bsn = models.CharField(max_length=20, verbose_name="BSN")
    iban_number = models.CharField(max_length=34, verbose_name="IBAN Number")
    nationality = models.CharField(max_length=100, verbose_name="Nationality")
    number_id = models.CharField(max_length=50, verbose_name="Number ID")
    id_date_of_expiry = models.DateField(verbose_name="ID Date of Expiry")
    
    MARITAL_STATUS_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Registered Partnership", "Registered Partnership"),
        ("Divorced", "Divorced"),
        ("Living Together Without Contract", "Living Together Without Contract"),
    ]
    marital_status = models.CharField(
        max_length=50, 
        choices=MARITAL_STATUS_CHOICES, 
        verbose_name="Marital Status"
    )
    name_spouse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name of Spouse (if married)")
    
    TRAVEL_METHOD_CHOICES = [
        ("Car", "Car"),
        ("Public Transport", "Public Transport"),
        ("Bicycle", "Bicycle"),
    ]
    travel_to_work = models.CharField(
        max_length=20, 
        choices=TRAVEL_METHOD_CHOICES, 
        verbose_name="How Do You Travel to Work?"
    )
    available_from_date = models.DateField(verbose_name="Available From What Date")
    shirt_size = models.CharField(max_length=10, blank=True, null=True, verbose_name="Shirt Size")
    trouser_size = models.CharField(max_length=10, blank=True, null=True, verbose_name="Trousers/Pants Size")
    
    # Document Fields
    id_front = models.ImageField(upload_to="documents/id/", blank=True, null=True, verbose_name="ID Front")
    id_back = models.ImageField(upload_to="documents/id/", blank=True, null=True, verbose_name="ID Back")
    bank_card = models.ImageField(upload_to="documents/bank_card/", blank=True, null=True, verbose_name="Bank Card")
    health_insurance_front = models.ImageField(upload_to="documents/health_insurance/", blank=True, null=True, verbose_name="Health Insurance Card Front")
    health_insurance_back = models.ImageField(upload_to="documents/health_insurance/", blank=True, null=True, verbose_name="Health Insurance Card Back")
    work_permit = models.FileField(upload_to="documents/work_permit/", blank=True, null=True, verbose_name="Work Permit")
    
    def __str__(self):
        return f"{self.official_given_names} {self.surnames}"
