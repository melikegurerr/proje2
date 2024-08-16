"""
URL configuration for first_project project.

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
from django.contrib import admin # Django'nun admin modülünü projeye dahil eder
from django.urls import path, include # URL tanımlamaları için gerekli fonksiyonları projeye dahil eder

urlpatterns = [
    path('admin/', admin.site.urls), # 'admin/' URL'sine gelen istekleri Django'nun admin paneline yönlendirir
    path("", include("code4us.urls")), # Ana sayfadan başlayan tüm URL isteklerini 'code4us' uygulamasının URL tanımlamalarına yönlendirir
]

