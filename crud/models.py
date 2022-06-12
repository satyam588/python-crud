from statistics import mode
from django.db import models

# Create your models here.
class tbl_student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12)
    city = models.CharField(max_length=255)
    address = models.TextField()
    created_on = models.DateField()

    def __str__(self) -> str:
        return self.name
