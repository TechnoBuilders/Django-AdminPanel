from django.db import models

class RFQReceived(models.Model):
    idNumber = models.BigAutoField(primary_key=True)
    partNumber = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=20)
    description = models.TextField()
    quantityRequired = models.IntegerField()
    UOM = models.TextField()
    leadTime = models.DateField()
    remarks = models.TextField()
