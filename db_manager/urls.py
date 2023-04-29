from django.urls import path
from . import views

urlpatterns = [
    path('charity_list/', views.charity_list, name='charity_list'),
    path('charity_list/<int:pk>/', views.charity_list, name='charity_edit'),
    path('charity_delete/<int:pk>/', views.charity_delete, name='delete_charity'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_list/<int:pk>/', views.user_list, name='user_edit'),
    path('user_delete/<int:pk>/', views.user_delete, name='delete_user'),
]