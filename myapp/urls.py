from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('home', views.home, name='home'),
    
    path('menu', views.menu,name='menu'),
    path('reservations', views.reservations,name='reservations'),
    path('contact', views.contact,name='contact'),
    path('gallery', views.gallery,name='gallery'),
    path('signup', views.handleSignup, name='handlesSignup'),
    path('login', views.handlelogin, name='handleslogin'),
    path('logout', views.handlelogout, name='handleslogout'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('desserts/', views.desserts, name='desserts'),
    path('vegetarian/', views.vegetarian, name='vegetarian'),
    path('non_veg/', views.non_veg, name='non_veg'),
    path('drink/', views.drink, name='drink'),
    path('fast_food/', views.fast_food, name='fast_food'),
    path('seafood/', views.seafood, name='seafood'),

]
