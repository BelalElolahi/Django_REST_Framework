from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions
from  .serializer import PhoneSerializer
from .permissions import IsOwnerOrReadOnly

from phone.models import Phone
# Create your views here.

class PhoneList(generics.ListCreateAPIView):
    queryset= Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes= (IsOwnerOrReadOnly,)

class PhpneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Phone.objects.all()
    serializer_class= PhoneSerializer
    permission_classes= (IsOwnerOrReadOnly,)
