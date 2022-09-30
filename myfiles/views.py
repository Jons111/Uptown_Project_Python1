from django.shortcuts import render

# Create your views here.

def index(malumot):
    return render(malumot,'index.html')