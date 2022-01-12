from django.shortcuts import render
from django.http import HttpResponse
from .models import cars


# Create your views here.
def index(request):
    Cars = cars.objects.all() 
    context = {'Cars': Cars} 
    return render(request, 'f1_app/cars_extend.html', context) 