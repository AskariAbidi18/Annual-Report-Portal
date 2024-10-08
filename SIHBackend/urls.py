"""
URL configuration for SIHBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Authentication import views

from django.urls import path
from Authentication.views import download_pdf


urlpatterns = [
    path('admin/download-report/', download_pdf, name='download_pdf'),
    path('django-admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('index/',views.HomePage,name='index'),
    path('admin/',views.AdminPage,name="admin"),
    path('logout/', views.LogoutPage, name='logout'),  
    path('report/', views.report_view, name='report')
]


