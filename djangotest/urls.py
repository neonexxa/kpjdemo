"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from myapp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.root),
    path('home_menu/', views.home, name='home'),
    path('menu_doctor/',views.menu_doctor, name='menu_doctor'),
    path('menu_doctor_calling/',views.menu_doctor_calling, name='menu_doctor_calling'),
    path('menu_nurse_calling/',views.menu_nurse_calling, name='menu_nurse_calling'),
    path('menu_doctor_mytreatment/',views.menu_doctor_mytreatment, name='menu_doctor_mytreatment'),
    path('menu_doctor_myprofile/',views.menu_doctor_myprofile, name='menu_doctor_myprofile'),
    path('menu_tv/',views.menu_tv, name='menu_tv'),
    path('webhook/', csrf_exempt(views.webhook), name='webhook'),
]