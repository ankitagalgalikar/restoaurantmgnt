#superuserpassword:-12345
#username-person

# Create your views here.

import random
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Restoapp.models import Order,Product,Cart
from django.db.models import Q

# Create your views here.

def home(request):
    userdata=request.user.id
    # print('userdata id:',userdata)
    # print('userdata id:',request.user.is_authenticated)
    obj=Product.objects.filter(is_active=True)
    context={'product':obj}
    return render(request,'index.html',context)

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        c=request.POST['ucpass']
        uobj=User.objects.create(username=u,email=u)

        #set password method is used to convert password into encrypted form
        uobj.set_password(p)
        uobj.save()
        return redirect('/register')

def  user_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        a=authenticate(username=u,password=p)
        if a is not None:
            print(a)
            print(a.password,a.id)
            login(request,a)
            return redirect('/')
        else:
            print(a)
            return HttpResponse('Login Fail')

        return HttpResponse('Hello '+u)
    
def user_logout(request):
    logout(request)
    return redirect('/')

def product_detail(request,pid):
    obj=Product.objects.filter(id=pid)
    context={'product':obj}
    return render(request,'fooddetail.html',context)

def addtocart(request,pid):
    userid=request.user.id
    u=User.objects.filter(id=userid)
    p=Product.objects.filter(id=pid)
    c=Cart.objects.create(uid=u[0],pid=p[0],cprice=p[0].price)
    c.save()
    return redirect('/cart')

def cart(request):
    c=Cart.objects.filter(uid=request.user.id)
    s=0
    cnt=0
    for i in c:
        cnt+=1
        s=s+(i.pid.price * i.qty)
    context={'product':c,'total':s,'cnt':cnt}
    print('sum:',s)
    return render(request,'cart.html',context)

def updateqty(request,qv,cid):
    c=Cart.objects.filter(id=cid)
    if qv=='1':
        qty=c[0].qty+1
        c.update(qty=qty)
        return redirect('/cart')
    elif c[0].qty>1:
        qty=c[0].qty-1
        c.update(qty=qty)
        return redirect('/cart')

    else:
        return redirect('/cart')
    
def catfilter(request,cv):
    if cv=='1':
        obj=Product.objects.filter(cat=1)
        context={'product':obj}
        return render(request,'index.html',context)
    elif cv==2:
        obj=Product.objects.filter(cat=2)
        context={'product':obj}
        return render(request,'index.html',context)

    else:
        obj=Product.objects.filter(cat=3)
        context={'product':obj}
        return render(request,'index.html',context)

def range(request):
    if request.method=='GET':
        min=request.GET['min']
        max=request.GET['max']
        # select pname from products where price>=max and price<=max
        c1=Q(price__gte=min)
        c2=Q(price__lte=max)
        obj=Product.objects.filter(c1 & c2)
        context={'product':obj}
        return render(request,'index.html',context)

def placeorder(request):
    c=Cart.objects.filter(uid=request.user.id)
    oid=random.randrange(1000,9999)
    print(oid)
    for x in c:
        obj=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        obj.save()
        x.delete()
        return redirect('/makepayment')
    
import razorpay
def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_zkVM1TybBgfQwx", "fYo5WKtMkjz76nEqeuv5TfcY"))
    obj=Order.objects.filter(uid=request.user.id)
    s=0
    for i in obj:
        s=s+(i.pid.price*i.qty)
        oid=i.order_id
    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    print(payment)
    context={'data':payment}
    return render(request,'pay.html',context)

def removecart(request,cid):
    c=Cart.objects.get(id=cid)
    c.delete()
    #c=Cart.objects.delete(cid)
    return redirect('/cart')

def contact(request):

    return render(request,'contact.html')

def about_us(request):

    return render(request,'about.html')
    
def forget_password(request):
    if request.method=='GET':
        return render(request,'login')
    
    else:
        

    
