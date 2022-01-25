from django.contrib import admin
from django.urls import path
from basic_app import views


app_name = 'basic_app'

#url
urlpatterns = [
    path('', views.index , name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout , name='user_logout'),
    path('special/',views.special , name = 'special'),
    path('login/',views.user_login ,name='user_login')

]
