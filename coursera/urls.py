from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('hello/',views.say_hello,name="hello"),
    path('homepage/',views.homepage,name="homepage"),
    path('date/',views.display_date,name="display"),
    path('menu/',views.menu,name='menu'),
]