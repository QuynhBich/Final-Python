"""Accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
]+ static(settings.WALLPAPER_FILES, document_root=settings.WALLPAPER_URL)
