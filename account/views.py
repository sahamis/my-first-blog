from django.shortcuts import render

def user_new(request):
  return render(request, "user/new.html")
