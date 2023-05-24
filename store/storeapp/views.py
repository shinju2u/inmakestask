from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request , "home.html")

def login(request):
    return render(request , "login.html")

def register(request):
    return render(request , "register.html")
def product(request):
    if request.method == 'POST':
        # Process the form data here

        # Show success message
        messages.success(request, 'Order Confirmed!')
        return redirect('product')  # Redirect to the same page to clear the form and show the message

    return render(request, "product.html")