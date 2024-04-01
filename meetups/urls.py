from . import views # Importing the views.py file in the app folder. is for the same folder
# * Link or register all the app functions and classes and execute the urls. *
from django.urls import path,include
# linking all classes or functions from the app views file to this file. using views.function/class name.

urlpatterns = [
    path('meetups/',views.index,name = 'all-meetups'),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name = 'meetup-detail'),
    path('meetups/success',views.confirm_registration, name = 'confirm-registration'),
] # our-domain.com/meetups/ this path will become active
# name is unique identifier. name is useed in html file href {% url 'meetup-detail'%} 
# link this paths to project urls.py file

# add appname in the settings.py in installed_apps 

