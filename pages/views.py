from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")

def notavailable(request):
    return render(request, 'pages/notavailable.html')

def signUpView(request):
    return render(request, 'pages/signup.html')

def register(request):
    person = Person.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), password=request.POST.get('password'))
    person.save()

    return redirect('/pages/signin')

def signInView(request):
    return render(request, 'pages/signin.html')

def login(request):
    email=request.GET.get('email')
    password=request.GET.get('password')
    if Person.objects.filter(email=request.POST.get('email')).exists():
        personLoggedIn = Person.objects.get(email=request.POST.get('email'), password=request.POST.get('password'))
        request.session['person'] = personLoggedIn.id
        return redirect('/pages/myreservations/{}'.format(personLoggedIn.id))
    else:
        return HttpResponse("User not found. Try again!")
    
def logout(request):
    request.session.clear()
    request.session.flush()
    return redirect('/pages/signin')


def myReservationsView(request, person_id): 
    person = Person.objects.get(id=person_id)
   
    """ personId = request.session['person']
    if personId != person_id: 
        return HttpResponse("No rights!") """
    
    messages = Message.objects.all()
    cottages = Cottage.objects.all()
    reservations = Reservation.objects.filter(person=person)
    return render(request, 'pages/myreservations.html', {'person': person.name, 'cottages': cottages, 'messages': messages, 'reservations': reservations})

#@transaction.atomic
def book(request): 
    if 'person' not in request.session:
        return HttpResponse("User not found. Please sign in!")
    else:    
        personId = request.session['person'] 
        person = Person.objects.get(id=personId)
        cottage = Cottage.objects.get(name=request.GET.get('cottage'))
        dateFrom = datetime.strptime(request.GET.get('dateFrom'), '%Y-%m-%d').date()
        dateTo = datetime.strptime(request.GET.get('dateTo'), '%Y-%m-%d').date()

        cottageReservations = Reservation.objects.filter(cottage=cottage)
        for reservation in cottageReservations:
            resDateFrom = reservation.date_from
            resDateTo = reservation.date_to
            if (dateFrom == resDateFrom and dateTo == resDateTo) or (dateFrom > resDateFrom and dateFrom < resDateTo) or (dateTo > resDateFrom and dateTo < resDateTo) or (dateFrom < resDateFrom and dateTo < resDateTo and dateTo > resDateFrom) or (dateFrom < resDateFrom and dateTo > resDateTo):
                return redirect('/pages/notavailable')
        
        count = ((dateTo - dateFrom).days) * Cottage.objects.get(name=request.GET.get('cottage')).rent
        
        request.session['cottage'] = cottage.name
        request.session['dateFrom'] = dateFrom.strftime('%Y-%m-%d')
        request.session['dateTo'] = dateTo.strftime('%Y-%m-%d')
        request.session['count'] = count

        return render(request, 'pages/thankyou.html', {'person': person, 'count': count, 'cottage': cottage, 'dateFrom': dateFrom, 'dateTo': dateTo})

def confirm(request):
    """ if 'person' not in request.session:
        return HttpResponse("User not found. Please sign in!") """
    """ else:     """
    personId = request.session['person']
    person = Person.objects.get(id=personId)

    reservation = Reservation.objects.create(cottage=Cottage.objects.get(name=request.session['cottage']),
    person=person, date_from=request.session['dateFrom'], 
    date_to=request.session['dateTo'], count=request.session['count'])

    reservation.save()
    person = Person.objects.filter(id=personId).update(ssn=request.POST.get('ssn'))
    
    return redirect('/pages/myreservations/{}'.format(personId))

def message(request):
    message = Message.objects.create(content=request.POST.get('content'), sender=request.POST.get('sender'))
    return HttpResponse("Thank you! Your message is saved.")

def cancel(request, reservation_id):
    if 'person' not in request.session:
        return HttpResponse("User not found. Please sign in!")
    else:  
        if Reservation.objects.filter(id=reservation_id).exists():
            reservation = Reservation.objects.get(id=reservation_id)
            
            """ personId = request.session['person']
            person = Person.objects.get(id=personId)
            if reservation.person != person:
                return HttpResponse("No rights!")
            else:  """

            reservation.delete()
            return HttpResponse("Thank you! Your reservation is cancelled.")
        else:
            return HttpResponse("Your reservation is already cancelled.")
    