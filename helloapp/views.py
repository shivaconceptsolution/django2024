from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
def index(request):
    return HttpResponse('Hello World')
def addition(request):
    if request.method=='POST':
        a,b = int(request.POST['txtnum1']),int(request.POST['txtnum2'])
        c=a+b
        return render(request,'helloapp/addition.html',{'key':c})
    else:
        return render(request,'helloapp/addition.html')

def reg(request):
    if request.method=='POST':
        #obj = Register(username=request.POST['txtuser'],emailid=request.POST['txtemail'],password=request.POST['txtpass'],mobile=request.POST['txtmobile'],fullname=request.POST['txtfname'])
        #obj.save()
        user = User.objects.create_user(request.POST['txtuser'],request.POST['txtemail'],request.POST['txtpass'])
        user.first_name=request.POST['txtfirst']
        user.last_name=request.POST['txtlast']
        user.save()
        return render(request,"helloapp/reg.html",{"key":"data inserted successfully"})
    else:
        return render(request,"helloapp/reg.html")
def viewreg(request):
    if request.user.is_authenticated:
      obj = Register.objects.all()
      return render(request,"helloapp/viewreg.html",{"key":obj})
    else:
        return redirect('/helloapp/loginuser')

def loginuser(request):
    if request.method=='POST':
        obj = authenticate(username=request.POST['txtemail'],password=request.POST['txtpass'])
        if obj is not None:
            login(request,obj)
            #request.session['uid']=request.POST['txtemail']
            return redirect('/helloapp/viewreg')
        else:
            return render(request,"helloapp/login.html",{"key":"invalid emailid and password"})
    else:
        return render(request,"helloapp/login.html")
def logoutuser(request):
    #del request.session['uid']
    logout(request)
    return redirect('/helloapp/loginuser')

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('ckey', 'hello')
    return response

def getcookie(request):
    a  = request.COOKIES['ckey']
    return HttpResponse("value is "+  a)

def ajaxload(request):
    return render(request,"helloapp/search.html")
def ajaxcode(request):
    data = request.GET["q"]
    result=Register.objects.filter(fullname__startswith=data)
    return render(request,"helloapp/searchresult.html",{"key":result})