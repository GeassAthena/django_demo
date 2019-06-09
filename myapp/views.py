from django.shortcuts import render
from myapp import models


# Create your views here.


def index(request):
    # request.POSTd
    # return HttpResponse("hello world!")
    global user_list
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 插入一条数据
        models.UserInfo.objects.create(username=username, password=password)
        print(username, password)
        # 从数据库读取所有数据
        user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})
