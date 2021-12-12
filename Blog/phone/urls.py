from django.urls import path
from .views import PhoneList , PhpneDetail


urlpatterns = [
    path('',PhoneList.as_view(),name='phone_list'),
    path('<int:pk>' , PhpneDetail.as_view(),name='phone_detail')
]