from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import User
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        print(request.POST,'data')
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            return redirect('home')
        else:
            print('some thing went wrong')
            
    else:
      pass
  
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)

        user = auth.authenticate(email=email, password=password)
        print(user,'user')

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'Login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    return redirect('login')
