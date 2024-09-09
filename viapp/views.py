from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'login.html')
    
def dashboard(request):
    iv_bag_percentage = 75

    return render(request, 'dashboard.html', {
        'iv_bag_percentage': iv_bag_percentage
    })

def logout_view(request):
    logout(request)
    return redirect('home')

