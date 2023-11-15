from nz.views import *
from django.urls import path

app_name = 'nz'

urlpatterns = [
    path('willi/',willi,name='willi'),
    path('ravi/',ravi,name='ravi'),
]