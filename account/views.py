from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def user_new(request):
  return render(request, "user/new.html")

def user_show(request, pk):
  user = get_object_or_404(User, pk=pk)
  return render(request, "user/show.html", {"user": user})