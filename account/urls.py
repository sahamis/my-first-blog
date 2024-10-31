from django.urls import path
from . import views

urlpatterns = [
  path("signup", views.user_new, name="user_new")
]