from tkinter import CASCADE
from django.db import models

class RFQReceived(models.Model):
    idNumber = models.BigAutoField(primary_key=True)
    partNumber = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    description = models.TextField()
    quantityRequired = models.IntegerField()
    UOM = models.CharField(max_length = 20, default='Nos', help_text = 'Units of Measurement')
    leadTime = models.DateField()
    remarks = models.TextField()
    RFQNumber = models.CharField(max_length = 30, blank = True)
    OfficerName = models.CharField(max_length = 50, blank = True)
    DateOfRFQ = models.DateField( auto_now_add = True)
    ClosureOfRFQ = models.DateField(null = True)
    AlternatePartNumber = models.CharField(null =True, max_length = 30)
    TargetPrice = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
    RFQNotes = models.TextField(null = True)
    isActive = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.manufacturer + '-' + self.partNumber
    
class ClientQuatation(models.Model):
    CURRENCY_CHOICE = (
        ('RS', 'Rupees'),
        ('USD', 'US Dollars'),
        ('AUD', 'Australian Dollars')
    )
    quoteNumber = models.BigAutoField(primary_key=True)
    partNumber = models.ForeignKey(RFQReceived, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=30)
    description = models.TextField()
    UOM = models.CharField(max_length = 20, default='Nos', help_text = 'Units of Measurement')
    SPQ = models.IntegerField(default=0, help_text = 'Factory packed quantity')
    MOQ = models.IntegerField(default= 0, help_text = 'Minimum order to be placed')
    UnitPrice = models.DecimalField(null = False, decimal_places = 2, max_digits = 10)
    PriceInclusiveTaxes = models.BooleanField(default=True)
    Currency = models.CharField(max_length= 10, choices=CURRENCY_CHOICE, default='RS')
    INCOTERMS = models.TextField(null = True)
    isActive = models.BooleanField(default = True)