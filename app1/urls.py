app1="anything"
from django.urls import path

from app1.views import *
urlpatterns = [
    path('Msd/',Msd,name='Msd'),
]

