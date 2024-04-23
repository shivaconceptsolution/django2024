from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('ram', views.addition, name='addition'),
path('reg', views.reg, name='reg'),
path('loginuser', views.loginuser, name='loginuser'),
path('logoutuser', views.logoutuser, name='logoutuser'),
path('getcookie', views.getcookie, name='getcookie'),
path('setcookie', views.setcookie, name='setcookie'),
path('viewreg', views.viewreg, name='viewreg'),
path('ajaxload',views.ajaxload,name='ajaxload'),
path('ajaxcode',views.ajaxcode,name='ajaxcode'),
path('ajaxcode1',views.ajaxcode1,name='ajaxcode1')

]
