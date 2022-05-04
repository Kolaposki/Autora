from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('success/', success, name='success'),
    path('checkout/', checkout, name='checkout'),
    path('service-details/<slug:slug>', service_detail, name='service_detail'),

]
