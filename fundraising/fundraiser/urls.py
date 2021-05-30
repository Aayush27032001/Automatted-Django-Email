from django.contrib import admin
from django.urls import path, include
from fundraiser import views

urlpatterns = [
    path('',views.index, name="home"),
    path('donate',views.donate, name="donate"),

]