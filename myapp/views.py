from django.shortcuts import render

from .models import Course

def course(request):
    cours = Course.objects.all()
    return render(request,'myapp/index.html',{'cours': cours})

def link_a(request,id):
    course = Course.objects.get(id=id)
    return render(request,'myapp/link_a.html',{'cours': course})
