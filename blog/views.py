from django.shortcuts import render, get_object_or_404
from .models import News
from django.http import HttpResponse, Http404


def index(request):
    news = News.objects.all()
    return render(request, "blog/news.html", {"news": news})
