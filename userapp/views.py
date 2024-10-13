from django.shortcuts import render, redirect
from .forms import LoginForm
from django .http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                return redirect('login')
            
            login(request,user)
            return redirect('home')
            

    form = LoginForm()
    return render(request, 'login.html',{'form':form})

@login_required
def home_view(requst):
    return render(requst, 'home.html')