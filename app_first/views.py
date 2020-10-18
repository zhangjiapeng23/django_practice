from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from app_first.models import User, Books
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
            if len(User.objects.all().filter(user_name=user_name)) != 0:
                return HttpResponse("user name is exist!")
            else:
                user_info = User.objects.create(user_name=user_name, password=password)
                print(user_info.user_name, user_info.password)
            return render(request, 'login.html')
        else:
            return HttpResponse("user name or password is blank!!")

    else:
        return render(request, 'register.html')


def books(request):
    books = Books.objects.all()
    if books.count() > 0:
        for book in books:
            book_id = book.id
            book_name = book.book_name
            book_price = book.price
            book_publish_date = book.publish_date
            book_press = book.press
            print(book_id, book_name, book_price, book_publish_date, book_press)
    else:
        books = None
    return render(request, 'books.html', {'books': books})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    elif request.method == 'POST':
        book_name = request.POST.get('book_name')
        price = float(request.POST.get('price'))
        publist_date = request.POST.get('publish_date')
        publist_date = datetime.strptime(publist_date, '%Y%m%d')
        publist_date = publist_date.strftime('%Y-%m-%d')
        press = request.POST.get('press')
        Books.objects.create(book_name=book_name, price=price, publish_date=publist_date, press=press)
    return redirect('/app_first/books')



def remove_book(request, id: int):
    res = Books.objects.all().filter(id=id)
    if res:
        res.delete()
    else:
        print("Not find this book!")
    return redirect('/app_first/books')

def edit_book(request, id: int):
    if request.method == 'GET':
        book = Books.objects.all().filter(id=id)
        if book:
            return render(request, 'edit_book.html', {'book': book[0]})
        else:
            print("Not find this book!")
    elif request.method == 'POST':
        book_name = request.POST.get('edit_name')
        price = request.POST.get('edit_price')
        publish_date = request.POST.get('edit_date')
        publish_date = datetime.strptime(publish_date, "%Y%m%d")
        publish_date = publish_date.strftime("%Y-%m-%d")
        press = request.POST.get('edit_press')
        Books.objects.all().filter(id=id).update(book_name=book_name, price=price, publish_date=publish_date,
                                                 press=press)

    return redirect('/app_first/books')




