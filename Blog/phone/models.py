from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Phone(models.Model):

    phone_name = models.CharField(max_length=155)
    phone_type = models.CharField(max_length=155)
    phone_ID = models.IntegerField()  
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.phone_name