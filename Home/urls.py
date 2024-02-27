from django.urls import include,path
from Home import views

urlpatterns =[
path('',views.Home,name= 'Home'),

]