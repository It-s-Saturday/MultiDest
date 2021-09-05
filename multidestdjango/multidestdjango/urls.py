"""multidestdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', TemplateView.as_view(template_name='index.html')),  # "home"/"landing" page
    path('parse_function', views.parse_function),  # adding paths means having the / after the URL
                                                   # i.e. 127.0.0.1:8000/parse_function will run parse_function()
                                                   # in views.py
    # path('show_results', views.show_results),
    # path('results', views.results),
    path('csrf/', views.csrf),
    path('ping/', views.ping),
]
