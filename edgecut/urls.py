from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('about.html',views.about,name='about'),
    path('furniture.html',views.furniture,name='furniture'),
    path('blog.html',views.blog,name='blog'),
    path('contact.html',views.contact,name='contact'),



]