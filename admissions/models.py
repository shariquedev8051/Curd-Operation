from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import DateField

# Create your models here.

class Common (models.Model):
    def __str__(self):
        return f'{self.__dict__}'
    
    def __repr__(self):
        return str(self)

    class Meta:
        abstract = True

DEPT = (( 0, "Select"),(1, "Software Testing"), (2,"Web Development"),(3,"SAP"),(4,"Other"))

class Admission(Common):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100,choices=DEPT,null=False,default="None")
    email = models.EmailField()
    mobile = models.BigIntegerField(db_column="Mobile No.")
    admission_date = models.DateField()
    identification_photo = models.ImageField(upload_to='media',null= True)

    class Meta:
        db_table = "students"