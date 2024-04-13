from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('ram', views.addition, name='addition'),
path('reg', views.reg, name='reg'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('viewreg', views.viewreg, name='viewreg')
]
