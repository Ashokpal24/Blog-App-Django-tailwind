"""
URL configuration for blog_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from blog.views import home as home_view
from blog.views import blog_by_id as blog_by_id_view
from auth.views import (login_user,logout_user,register_user)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/login/",login_user,name="login"),
    path("blog/logout/",logout_user,name="logout"),
    path("blog/register/",register_user,name="register"),
    path("",home_view,name="home"),
    path("blog/detail/<int:id>",blog_by_id_view,name="blog_details"),
    path("__reload__/", include("django_browser_reload.urls")),
]
