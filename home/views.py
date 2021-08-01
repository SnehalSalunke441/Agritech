from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def landing(request):
    return render(request,'landing.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/landing")
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has  been sent !')
    return render(request, 'contact.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        user = User.objects.create_user(first_name=first_name,email=email,username=username,password=password)
        user.save()
        messages.success(request, 'Your Account has  been created. Please Login')
        return render(request,'login.html')
    else:
        return render(request,'signup.html')

def logoutuser(request):
    logout(request)
    return redirect("/landing")

def about(request):
    return render(request, 'about.html')
    
def crops(request):
    return render(request, 'crops.html')

def pesticides(request):
    return render(request, 'pesticides.html')

def fertilizers(request):
    return render(request, 'fertilizers.html')    

def moderntech(request):
    return render(request, 'moderntech.html')

def wheat(request):
    return render(request, 'wheat.html')

def rice(request):
    return render(request, 'rice.html')

def onion(request):
    return render(request, 'onion.html') 

def orange(request):
    return render(request, 'orange.html')

def corn(request):
    return render(request, 'corn.html')  

def marigold(request):
    return render(request, 'marigold.html')      

def urea(request):
    return render(request, 'urea.html')      

def nitrophosphate(request):
    return render(request, 'nitrophosphate.html')      

def dap(request):
    return render(request, 'dap.html')      

def ssp(request):
    return render(request, 'ssp.html')      

def herbicides(request):
    return render(request, 'herbicides.html')      

def insecticides(request):
    return render(request, 'insecticides.html')              

def fungicides(request):
    return render(request, 'fungicides.html') 

def indoorvp(request):
    return render(request, 'indoorvp.html')        

def farmauto(request):
    return render(request, 'farmauto.html')

def greenhousefarm(request):
    return render(request, 'greenhousefarm.html')







