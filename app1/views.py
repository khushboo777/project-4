from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Msd(request):
    return HttpResponse("<h1>Msd is best captain</h1>")
