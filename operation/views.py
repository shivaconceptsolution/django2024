from django.shortcuts import render
data=''
def index(request):
    global data
    if request.method=='POST':
        a=request.POST.get('btnsubmit')
        if(a=='='):
            data=eval(data)
        else:
            data=data+a
        return render(request,"operation/index.html",{"result":data})

    else:
      return render(request,"operation/index.html")
def radioexample(request):
    if request.method=="POST":
        if request.POST.get('course')=='basic':
            data=['c','c++','ds']
        else:
            data=['java','python']
    return render(request,"operation/radio.html",{"res":data})
        
    return render(request,"operation/radio.html")
