from django.shortcuts import render

# Create your views here.

def post_list(request):
  return render(request, "blog/post_list.html", {}) #受け取ったリクエストを元にテンプレートを作成