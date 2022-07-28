"""notes_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from notes import views

app_name = 'notes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.registration, name='registrations'),
    path('current/', views.currentuser, name='current'),
    path('complated/', views.complated, name='complated'),
    path('', views.home, name='home'),
    path('testapi/', include('notes.urls')),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('create/', views.createnotes, name='createnotes'),
    path('todoviews/<int:todo_pk>', views.todoviews, name='todoviews'),
    path('todoviews/<int:todo_pk>/completed', views.completed, name='completed'),
    path('todoviews/<int:todo_pk>/deleted', views.deleted, name='deleted'),
]
