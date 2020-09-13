from django.shortcuts import render
from django.http import HttpResponse

from app_first.models import User
# Create your views here.


def index(request):

    return HttpResponse("index page")


def test(request):

    return HttpResponse("Test page")


def login(request):
    import time
    ctime = time.strftime('%Y/%m/%d-%H:%M:%S')
    if request.method == 'POST':
        if request.POST.get('username') == 'james' and request.POST.get('password') == '111111':
            return HttpResponse("login success!")
        else:
            return HttpResponse('username or password is incorrect!')
    else:
        return render(request, 'login.html', {'time': ctime})


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if user_name != '' and password != '':
            User.objects.create(user_name=user_name, password=password)
            return render(request, 'login.html')
        else:
            return HttpResponse("user name or password is blank!!")

    else:
        return render(request, 'register.html')



