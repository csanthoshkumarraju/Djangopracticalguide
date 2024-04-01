from django.contrib import admin
from .models import Meetup,Participant

# importing Meetup class or model from models.py to here . is for same folder
# using admin page admin can manage models.py file and database.
# create a superuser and creds
# python3 manage.py createsuperuser
# give username and password
# use this logins in "http://127.0.0.1:8000/admin/" to go to admin page
# Register your models here.
# created class or models in models.py need to register here to work.

# MeetupAdmin list_display displaying models.py Meetup class variable values

class MeetupAdmin(admin.ModelAdmin):
      list_display = ('title','location','date')
      list_filter = ('title','date') 
      prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Participant)




