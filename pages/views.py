from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")


def signUpView(request):
    return render(request, 'pages/signup.html')

def register(request):
    person = Person.objects.create(name=request.GET.get('name'), email=request.GET.get('email'), password=request.GET.get('password'))
    person.save()

    return redirect('/pages/')

def signInView(request):
    return render(request, 'pages/signin.html')

def login(request):
    personLoggedIn = Person.objects.get(email=request.GET.get('email'), password=request.GET.get('password'))
    return redirect('/pages/myreservations/{}'.format(personLoggedIn.id))

def logout(request):
    request.session.flush()
    return redirect('/pages/signin')


def myReservationsView(request, person_id):
    person = Person.objects.get(id=person_id)
    reservations = Reservation.objects.filter(person=person)
    return render(request, 'pages/myreservations.html', {'reservations': reservations,'person': person})




