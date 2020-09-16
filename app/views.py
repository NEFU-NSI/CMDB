from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Domain
# Create your views here.

def default(request):
    return render(request,"home.html")   #主页面

def web_show(request):
    return render(request,"website.html") #网站总览

def department(request):
    return render(request,"department.html") #部门总览

def department_website(request):
    return render(request,"department_website.html") #部门下网页页面
 