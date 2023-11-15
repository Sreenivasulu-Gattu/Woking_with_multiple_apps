from django.urls import path
from India.views import *
app_name = 'India'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('kohli/',kohli,name='kohli'),
]