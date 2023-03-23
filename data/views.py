from django.shortcuts import render, redirect
from random import randint
from django.http import HttpResponse
from .models import person
from .models import data
from .models import nubm


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        person(username=username, password=password, userid=randint(60000,99999999)).save()

    return render(request, 'signin.html')


def add(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    s = person.objects.filter(username=username).all()
    for i in s:
        if i.password==password:
            id = i.userid

            return render(request, 'add.html')
        else:
            return HttpResponse('page not foud')

def saves(requset):
    if requset.method=="POST":
        savol = requset.POST['savol']
        javob = requset.POST['javob']
        user = requset.POST['user']

        data(froms=savol, to=javob, userid=user).save()
        s = person.objects.filter(username=user)
        for i in s:
            password=i.password
        return redirect(f'signin.html')