from django.contrib import admin

from django.urls import path

from .views import CharitiesViewSet, UserViewSet

urlpatterns = [
    path('charities/', CharitiesViewSet.as_view({
            'get':'list',
            'post':'create',
    })),
    path('charities/<str:pk>/', CharitiesViewSet.as_view({
            'get':'retrieve',
            'put':'update',
            'delete':'destroy',
    })),
    path('user/', UserViewSet.as_view({
            'get':'list',
            'post':'create',
    })),
    path('user/<str:pk>/', UserViewSet.as_view({
            'get':'retrieve',
            'put':'update',
            'delete':'destroy',
    })),

]

