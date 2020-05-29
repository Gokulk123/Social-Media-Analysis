"""analysisproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .analysisapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('register/',views.register,name="register"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('user/',views.user,name="user"),
    path('userhome/',views.userhome,name="userhome"),
    path('category_form/',views.category_form,name="category_form"),
    path('add_topics/',views.add_topics,name="add_topics"),
    path('results/', views.results, name="results"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('admin_add_topics/',views.admin_add_topics,name="admin_add_topics"),
    path('admin_analysis_result/', views.admin_analysis_result, name="admin_analysis_result"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('user_reg/', views.user_reg, name="user_reg"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('test/', views.testCode, name="testCode"),
    path('admin_posts/', views.admin_posts, name="admin_posts"),
    #path('our_posts/', views.our_posts, name="our_posts"),
    path('view_users/', views.view_users, name="view_users"),
    path('analysis/', views.analysis,name="analysis"),
    path('view_comments/', views.view_comments,name="view_comments"),
    path('user_posts/', views.user_posts,name="user_posts"),
    path('values/', views.values,name="values"),
    path('comments/', views.comments,name="comments"),
    path('our/', views.our,name="our"),
]
