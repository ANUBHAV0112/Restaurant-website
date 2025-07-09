# views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .models import Booking, Table
from .forms import TableReservationForm, BookingForm
from django.db import IntegrityError
import datetime

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def desserts(request):
    return render(request, 'desserts.html')

def vegetarian(request):
    return render(request, 'Vegetarian.html')

def non_veg(request):
    return render(request, 'Non_Veg.html')

def drink(request):
    return render(request, 'drink.html')

def fast_food(request):
    return render(request, 'fast_food.html')

def seafood(request):
    return render(request, 'seafood.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard or home
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        # Validate passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        
        # Check if user exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'signup.html')
        
        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')

def reservations(request):
    if request.method == "POST":
        form = TableReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']

            # Check if a reservation with this name, email, and date already exists
            if Table.objects.filter(name=name, email=email, date=date).exists():
                messages.error(request, "A reservation with this name and email for this date already exists.")
                return redirect('reservations')

            form.save()
            messages.success(request, "Reservation successfully saved!")
            return redirect('reservations')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TableReservationForm()

    return render(request, 'reservations.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Check if a booking with the same name and email already exists
            if Booking.objects.filter(name=name, email=email).exists():
                messages.error(request, "A booking with this name and email already exists.")
                return redirect('contact')

            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()

    return render(request, 'contact.html', {'form': form})

def gallery(request):
    return render(request, 'gallery.html')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname1']
        lname = request.POST['lname1']
        email = request.POST['email1']
        password1 = request.POST['password2']
        password2 = request.POST['password4']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers.")
            return redirect('home')

        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('home')

        myuser = User.objects.create_user(username=username, email=email, password=password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account is successfully created!")
        return redirect('home')

    return HttpResponse('404 not found')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password6']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('home')

    return HttpResponse('404 Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('home')


