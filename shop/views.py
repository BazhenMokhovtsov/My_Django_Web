from django.shortcuts import render, get_object_or_404
from .models import Course
from django.http import HttpResponse, Http404


# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):

# OPTIONS 1

    try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404()

# OPTION 2
# This option processes a 404 error without a block "try, expect"

    # course = get_object_or_404(Course, pk=course_id)
    # return render(request, 'shop/single_course.html', {'course': course})