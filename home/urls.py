from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
     path('', views.home, name='home'),
     path('tasks',views.tasks, name="tasks"),
     path('delete/<int:id>/', views.delete_view, name="deletedata"),
     path("deleteinfo/<int:id>",views.delete_info, name="deleteinfo"),
     path("contact/",views.contact, name="contact"),
     path("project/",views.project,name="project"),
     path("project2/",views.project2, name="project2")
]

