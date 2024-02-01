from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.welcome),
    path('hello/<str:name>/', views.hello_user),
    path('<int:number>/', views.one),
]