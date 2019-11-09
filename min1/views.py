from django.shortcuts import render

def home(request):
    return render(request, 'min1/home.html')