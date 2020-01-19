from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index')
