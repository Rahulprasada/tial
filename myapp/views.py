from django.shortcuts import render

def login(request):
    return render(request,"first.html")

def signup(request):
    return render(request,"second.html")