from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_1),
    path('group/<slug:slug>/', views.group_posts),
]