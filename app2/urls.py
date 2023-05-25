app2="something"
from django.urls import path
from app2.views import *

urlpatterns = [
    path('virat/',virat,name='virat')
    
]
