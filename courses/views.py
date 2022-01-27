from django.shortcuts import render, redirect
from .models import Courses, Semesters
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/login/')
def selectedCourses(request):
    ac = Courses.objects.all()
    cs = semester_year()
    if request.user.is_authenticated:
        # grabbing the user that currently logged in.
        user = User.objects.get(username=request.user.username)
        user.save()
        selected_courses = user.courses_set.all()
        if request.method == 'POST':
            selected_courses = request.POST.getlist('course')
            for sc in selected_courses:
                course = Courses.objects.get(course_name=sc)
                user.courses_set.add(course)
        return render(request, 'courses/courses.html', {'cs': cs, 'ac': ac, 'sc': user.courses_set.all()})


    else:
        return render(request, 'courses/courses.html', {'cs': cs, 'ac': ac})


def semester_year():
    today = datetime.datetime.today()
    year = str(today.year)[2:]
    if 9 <= today.month <= 12:
        semester = 'FA'
    elif 1 <= today.month <= 4:
        semester = 'SP'
    else:
        semester = 'SU'
        #    else:
        #        semester = 'WI'
    return semester + year


def remove_student(request):
    user = User.objects.get(username=request.user.username)
    remove_courses = request.POST.getlist('course')
    for check1 in remove_courses:
        course = Courses.objects.get(course_name=check1)
        user.courses_set.remove(course)
    return redirect('/courses')
