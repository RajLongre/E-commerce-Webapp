from django.shortcuts import render, HttpResponseRedirect
from .models import AllProduct,EachProductImage,Cart,Costumer,OrderPlaced
from .forms import Registration, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q



def index(request):
    if request.user.is_authenticated:
        user=(str(request.user)).upper()
        # user=user.upper()
        print(user)
        print(type(user))
        data1 = AllProduct.objects.filter(category="MensShirt")
        data2 = AllProduct.objects.filter(category="MensTshirt")
        data3 = AllProduct.objects.filter(category="WomensJacket")
        data4 = AllProduct.objects.filter(category="WomensSaree")



        return render(request, "estore/base.html",{"user":user,"data1":data1,"data2":data2,"data3":data3,"data4":data4})
    else:
        return HttpResponseRedirect("signin")
    


def tshirts(request):
    if request.user.is_authenticated:
        data = AllProduct.objects.filter(category="MensTshirt")
        return render(request, "estore/Tshirts.html", {"data": data})
    else:
        return HttpResponseRedirect("signin")


def shirts(request):
    if request.user.is_authenticated:
        data = AllProduct.objects.filter(category="MensShirt")
        return render(request, "estore/shirts.html", {"data": data,"active":"active"})
    else:
        return HttpResponseRedirect("signin")

def womens_jackets(request):
    if request.user.is_authenticated:
        data = AllProduct.objects.filter(category="WomensJacket")
        return render(request, "estore/womens_jackets.html", {"data": data,"active":"active"})
    else:
        return HttpResponseRedirect("signin")
    


def womens_saree(request):
    if request.user.is_authenticated:
        data = AllProduct.objects.filter(category="WomensSaree")
        return render(request, "estore/womens_saree.html", {"data": data})

    else:
        return HttpResponseRedirect("signin")

def KidsToy(request):
    if request.user.is_authenticated:
        data = AllProduct.objects.filter(category="KidsToy")
        return render(request, "estore/kids_toy.html", {"data": data})
    else:
        return HttpResponseRedirect("signin")
    


def buy_product(request, id):
    if request.user.is_authenticated:
        data = AllProduct.objects.get(pk=id)
        data1=EachProductImage.objects.get(pk=id)
        product_exist=False
        product_exist=Cart.objects.filter(Q(user=request.user)&Q(product=id)).exists()
        return render(request, "estore/buyshirt.html", {"data": data,"data1": data1,"product_exist":product_exist})
    else:
        return HttpResponseRedirect("signin")

    

def sign_up(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            form = Registration()
    else:
        form = Registration()
    return render(request, "estore/signup.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, "estore/signin.html", {"form": form})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("signin")

def search(req):
     if req.method=="POST":
         nm=req.POST.get('searchdata')
         
         data=AllProduct.objects.filter(name=nm)
         

         if data:
             return render(req,"estore/search.html",{'d1':data})
         
         else:
             return render(req,"estore/search.html",{'msg':"NO DATA AVAILABLE"})

def cart(request,id):
        user=request.user
        product=AllProduct.objects.get(pk=id)
        Cart(user=user,product=product).save()
        return HttpResponseRedirect("showcart")

def buynow(request,id):
        user=request.user
        product=AllProduct.objects.get(pk=id)
        Cart(user=user,product=product).save()
        return HttpResponseRedirect("checkout")
        
def showcart(request):
        tempamount=0
        amount=0
        user=request.user
        data=Cart.objects.filter(user=user)
        print(data)
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        if cart_product:
            counter=0
            for i in cart_product:
                counter=counter+1
                print(i.quantity)
                print(i.product.price)
                tempamount=(i.quantity*i.product.price)
                amount+=tempamount
            print(tempamount)
            print(amount)
            print(counter)

            return render(request,"estore/cart.html",{"data":data,"amount":amount,"counter":counter})
        
        else:
            return render(request,"estore/cart.html",{"MSG":"NO DATA, PLEASE ADD ITEMS IN CART"})
        # if cart_product is not None:




def profile(request):
     if request.method=="POST":
        # user=User.objects.filter(name=request.user)
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        locality=request.POST.get("locality")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        Costumer(user=request.user,name=name,contact=contact,locality=locality,city=city,pincode=pincode).save()
        return HttpResponseRedirect("address")
     return render(request,"estore/profile.html")

def address(request):
     
    user=request.user
    addresses=Costumer.objects.filter(user=user)
    # print(addresses)
    return render(request,"estore/address.html",{"addresses":addresses})

def checkout(request):
     
    tempamount=0
    amount=0
    data=Cart.objects.filter(user=request.user)
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
    counter=0
    print(cart_product)
    if cart_product:
            counter=0
            for i in cart_product:
                counter=counter+1
                print(i.quantity)
                print(i.product.price)
                tempamount=(i.quantity*i.product.price)
                amount+=tempamount
            print(tempamount)
            print(amount)
            print(counter)
    addresses=Costumer.objects.filter(user=request.user)
    
    

    return render(request,"estore/checkout.html",{"data":data,"amount":amount,"counter":counter,"addresses":addresses})
    


def orderplaced(request):
    # if request.method=="POST":
        
        costumerid=request.GET.get("addressbtn")
        costumer=Costumer.objects.get(pk=costumerid)
        cart=Cart.objects.filter(user=request.user)
        for i in cart:
            OrderPlaced(user=request.user,costumer=costumer,product=i.product,quantity=i.quantity).save()
            i.delete()
        return HttpResponseRedirect("order")
    
def order(request):
    
        data=OrderPlaced.objects.filter(user=request.user)
        return render(request,"estore/orderplaced.html",{"data":data})