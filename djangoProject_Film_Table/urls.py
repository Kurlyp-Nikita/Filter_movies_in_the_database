"""
URL configuration for djangoProject_Film_Table project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from film_table import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    path('films/', views.films, name='films'),
    path('films/add/', views.addfilms, name='addfilms'),
    path('films/del/<int:id>/', views.delete_film, name='delete_film'),
    path('films/edit/<int:id>/', views.edit_film, name='edit_film'),
    path('films/poisk/', views.poisk_film, name='poisk_film'),


]
