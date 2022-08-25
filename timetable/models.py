from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.



class Ferry(models.Model):

    name = models.CharField(max_length=30)
    date = models.DateField(null=True)
    time_departure = models.CharField(max_length=30, null=True)
    time_arrival = models.CharField(max_length=30, null=True)
    port_departure = models.CharField(max_length=30, null=True)
    port_arrival = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.name} {self.date} {self.time_departure} {self.port_departure} '


class Port(models.Model):

    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    boat = models.ManyToManyField(Ferry, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.country} '
