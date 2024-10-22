from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    context={"form":form}
    return render(request,"auth/register.html",context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request=request,username=username,password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'auth/login.html',{'error':"Invalid usename or password"})
    return render(request,'auth/login.html',{})

def logout_user(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')