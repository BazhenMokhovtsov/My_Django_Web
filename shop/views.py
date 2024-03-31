from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from datetime import datetime

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def time_now(request):
    current_datetime = datetime.now()
    print(current_datetime)  # Добавленная строка для проверки
    return render(request, 'base.html', {'current_datetime': current_datetime})