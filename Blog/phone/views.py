from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from  .serializer import PhoneSerializer

from phone.models import Phone
# Create your views here.

class PhoneList(generics.ListCreateAPIView):
    queryset= Phone.objects.all()
    serializer_class = PhoneSerializer


class PhpneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Phone.objects.all()
    serializer_class= PhoneSerializer
