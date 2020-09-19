from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Domain
# Create your views here.

def default(request):
    return render(request,"home.html")   #主页面

def web_show(request):
    website = Domain.objects.all()
    web_num = website.count()
    l=[]                                #l数列给出了某个网址的所有信息
    for x in range(len(website)):
        aweb = website[x]
        the_depart = aweb.department
        charger = Department.objects.filter(name = the_depart)[0].person_in_charge
        l.append([aweb,the_depart,charger])
    #     depart = Domain.objects.filter(id = depart_id)
    #     charger = depart.person_in_charge
    #     depart_name = depart.name
    #     l.append([website[x],charger,depart_name])
    context = {
        'website': website,           #website返回所有网址的查询对象  .domain_name查询域名  .department查询部门 .status查询状态
        'web_num': web_num,
        'web_info':l                   #web_info给出的是所有网址的全部信息
    }
    return render(request,"website.html",context=context) #网站总览

def department(request):
    depart_info = Department.objects.all()
    depart_num = depart_info.count()
    context = {
        'depart_info':depart_info,
        'depart_num': depart_num
    }
    return render(request,"department.html",context) #部门总览

def department_website(request):
    context = {}
    if request.method == 'POST':
        depart_name = request.POST.get('query')
        adepart = Department.objects.get(name = depart_name)
        depart_id = adepart.id
        webs = Domain.objects.filter(department_id = depart_id)
        count = webs.count()
        print(webs)
        context ={

            'depart_name':webs,
            'count':count
        }
    return render(request,"department_website.html",context) #部门下网页页面

def web_add(request):
    pass

def web_delete(request):
    pass

def web_search(request):
    pass

def depart_add(request):
    pass

def depart_delete(request):
    pass
