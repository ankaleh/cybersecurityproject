from django.urls import path

from . import views
from pages.views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signUpView, name='signup'),
    path('register/', register, name='register'),
    path('signin/', signInView, name='signin'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('myreservations/<int:person_id>', myReservationsView, name='myreservations'),
    path('book/', book, name='book'),
    path('message/', message, name='message'),
    path('cancel/<int:reservation_id>', cancel, name='cancel'),
    path('confirm/', confirm, name='confirm'),
    path('notavailable/', notavailable, name='notavailable')
    
]