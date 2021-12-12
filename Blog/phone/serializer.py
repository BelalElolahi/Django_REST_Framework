from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone_name','phone_type','phone_ID','owner']
        model = Phone