from tkinter import CASCADE
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

    def __str__(self) -> str:
        return self.manufacturer + '-' + self.partNumber
    
class ClientQuatation(models.Model):
    quoteNumber = models.BigAutoField(primary_key=True)
    partNumber = models.ForeignKey(RFQReceived, on_delete=models.CASCADE)