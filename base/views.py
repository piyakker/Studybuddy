from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home page')

def rooms(request):
    return HttpResponse('Rooms page')