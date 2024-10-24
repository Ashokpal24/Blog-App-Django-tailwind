from django.shortcuts import render, get_object_or_404
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

@login_required
def blog_by_id(request,id):
    blog=get_object_or_404(Blog,pk=id)
    context={"blog":blog}
    return render(request,"blog/details.html",context=context)