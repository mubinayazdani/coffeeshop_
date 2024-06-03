"""
URL configuration for coffeeshop project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='Master'),
    path('', views.Home, name='Home'),

    path('home/', views.Home, name='Home'),
    #Contact
    path('contact_us/', views.Contact_us, name='contact page'),
    #About
    path('about/', views.About, name='about'),
    #Service
    path('service/', views.Service, name='service'),
    #Menu
    path('menu/', views.Menu, name='menu'),
    #Reservation
    path('reservation/', views.Reserve, name='reserve'),
    #booking
    # path(r'^booking/', include('booking.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
