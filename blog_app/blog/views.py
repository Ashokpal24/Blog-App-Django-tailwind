from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog

# @login_required
# def hello_world(request):
#     return render(request,'home/index.html',{})

@login_required
def home(request):
    blogs=Blog.objects.all()
    context={"blogs":blogs}
    return render(request,'home/index.html',context=context)