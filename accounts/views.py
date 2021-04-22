from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import ImageForm
from .models import Image
from .location import Location

# Create your views here.
def indexView(request):
   
    return render(request,'index.html')
    
@login_required    
def dashboardView(request):
    return render(request,'dashboard.html')
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    latlon=[]
    for x in img:
        print(type(x.photo),"aaaaaaaaaaaaaaaaaaaaaaaaa")
        latlon.append(Location.location(x.photo))
    return render(request, 'myapp/home.html', {'img':img, 'form':form,'latlon':latlon})  
def registerView(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
       
    else:
        form = SignUpForm()    
    return render(request,'registration/register.html',{'form':form})     
  