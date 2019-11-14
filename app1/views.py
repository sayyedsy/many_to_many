from django.shortcuts import render
from .forms import bookform,authorform
from .models import book,author

# Create your views here.
def home(request):
    return render(request,'home.html')


def addbook(request):
    bf=bookform()
    return render(request,'addbook.html',{'bform':bf})