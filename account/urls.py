from django.urls import path
from . import views

urlpatterns = [
  path("signup", views.user_new, name="user_new"),
  path("user/<int:pk>", views.user_show, name="user_show")
]