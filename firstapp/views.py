from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    return render(request,"firstapp/home.html")


def Order(request):
    return render(request,"firstapp/order.html")


def Services(request):
    if request.method=="POST":
        user=User()
        requirements = request.POST.get("REQ")
        link = request.POST.get("LINK")
        quantity = request.POST.get("QUANTITY")
        name = request.POST.get("NAME")
        email = request.POST.get("EMAIL")
        number = request.POST.get("NUMBER")
        description = request.POST.get("DESC")
        user.requirements = requirements
        user.link = link
        user.quantity = quantity
        user.name = name
        user.email = email
        user.number = number
        user.description = description
        user.save()
        return render(request, "firstapp/order.html")
        
    
    return render(request, "firstapp/services.html")
