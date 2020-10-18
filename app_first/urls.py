from django.urls import path

from app_first import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('books/', views.books, name='books'),
    path('addbook/', views.add_book, name='add_book'),
    path('removebook/<int:id>', views.remove_book, name='remove_book'),
    path('editbook/<int:id>', views.edit_book, name='edit_book')


]
