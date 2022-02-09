from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('user/', views.user),
    path('sign_up/', views.sign_up)

]



