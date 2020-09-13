from django.urls import path

from app_first import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')

]
