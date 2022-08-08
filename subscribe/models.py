from django.db import models
from django.core.validators import MinLengthValidator
import sys
sys.path.append("..")
from timetable.models import Port
# Create your models here.

class Subscribers(models.Model):
    name = models.CharField(max_length=10, validators=[MinLengthValidator(1)])
    surname = models.CharField(max_length=40, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=100)
    destination = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True)
