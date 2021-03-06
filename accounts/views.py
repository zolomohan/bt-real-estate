from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        if password != password2:
            messages.error(request, "Passwords doesn't match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is used by another user.")
        else:
            user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            auth.login(request, user)
            messages.success(request, "Yay! You are now registered!")
            return redirect('index')
        # Redirects on Error
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You're Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contacted_at').filter(user_id=request.user.id)
    context = {
        "contacts": user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You're Logged Out")
        return redirect('index')
    return redirect('index')
