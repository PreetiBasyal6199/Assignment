import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class New_Data(models.Model):

    full_name=models.CharField(max_length=150)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10)
    salary=models.DecimalField(max_digits=5, decimal_places=2)
    designation=models.CharField(max_length=150)
    imported_by=models.CharField(max_length=100)
    imported_at=models.DateTimeField(auto_now=True,auto_now_add=False)

# class UserImportFile(models.Model):
#     # upload to MEDIA_ROOT/temp
#     user_import = models.FileField(upload_to="temp",
#                                       blank=False,
#                                       null=False)
    