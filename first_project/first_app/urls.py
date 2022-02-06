from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^index/', views.index),
    re_path(r'^hello/', views.say_hello),
    re_path(r'^.', views.any_response),

]