from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Register
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
        obj = Register(username=request.POST['txtuser'],emailid=request.POST['txtemail'],password=request.POST['txtpass'],mobile=request.POST['txtmobile'],fullname=request.POST['txtfname'])
        obj.save()
        return render(request,"helloapp/reg.html",{"key":"data inserted successfully"})
    else:
        return render(request,"helloapp/reg.html")
def viewreg(request):
    if(request.session.has_key('uid')):
      obj = Register.objects.all()
      return render(request,"helloapp/viewreg.html",{"key":obj})
    else:
        return redirect('/helloapp/login')

def login(request):
    if request.method=='POST':
        obj = Register.objects.filter(emailid=request.POST['txtemail'],password=request.POST['txtpass'])
        if obj.count()>0:
            request.session['uid']=request.POST['txtemail']
            return redirect('/helloapp/viewreg')
        else:
            return render(request,"helloapp/login.html",{"key":"invalid emailid and password"})
    else:
        return render(request,"helloapp/login.html")
def logout(request):
    del request.session['uid']
    return redirect('/helloapp/login')
