from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup
from .forms import ForRegistrationFormm

def index(request):    # index() is linked in meetups app in urls.py file
    #return HttpResponse("Hello world") 
    # meetups = [
    #     { 'title' : 'A first meetup' ,'location':'New York' , 'slug':'first'},
    #     { 'title' : 'A second meetup', 'location': 'Paris','slug': 'second' },
    # ]
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{'show_meetups':True,'meetups': meetups})  # html files linked here to render. 'meetups','show_meetups' are  keys given in index.html to get this dictionary'

def meetup_details(request,meetup_slug):
    # selected_meetup = {
    #     'title': 'A first meetup','description':'This is the first meetup'
    # }
    try:
        if request.method == 'GET':

            selected_meetup = Meetup.objects.get(slug = meetup_slug)
            registration_form = ForRegistrationFormm()
            
        else:
            registration_form = ForRegistrationFormm(request.POST)
            
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return redirect('meetups/registration-success.html')

        return render(request,'meetups/meetup-detail.html',{'meetup_title':selected_meetup.title,
                                                        'meetup_description':selected_meetup.description,
                                                        'meetup_location':selected_meetup.location,
                                                        'meetup_address':selected_meetup.address,
                                                        'date':selected_meetup.date,
                                                        'organizer_email':selected_meetup.organizer_email,
                                                        'form':registration_form,'meetup_found': True})
    except Exception as exc:
        return render(request,'meetups/meetup-detail.html',{'meetup_found':False})

def confirm_registration(request):
    return render(request,'meetups/registration-success.html')