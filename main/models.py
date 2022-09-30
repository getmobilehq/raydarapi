from django.db import models
import uuid
# Create your models here.


class InventoryData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    companyid = models.CharField(max_length=255)
    computer_data = models.JSONField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    
    
    