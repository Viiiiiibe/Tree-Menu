from django.urls import path
from . import views

urlpatterns = [
    path('<slug:active_slug>/', views.menus, ),
    path('', views.menus, name="index"),
]
