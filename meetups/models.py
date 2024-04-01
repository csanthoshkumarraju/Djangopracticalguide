from django.db import models
# **** register app name meetups in settings.py in installed appas. *******
# Create your models here.
#   models are created to store the data in database
# models can be managed in admin.py or website admin page
# Meetup is a table in database, title,slug are columns CharField integer field,TextField are datatype of columns
# quit control + c runserver
# --- Run the below commands ---
#  python3 manage.py makemigrations
#  python3 manage.py migrate 
# all the created classes or models need to register in the admin.py file.

class Participant(models.Model):
      email = models.EmailField(max_length=254,unique = True)
      def __str__(self):
            return self.email


class Meetup(models.Model):
      title = models.CharField(max_length=50)
      slug = models.SlugField(unique = True)
      description = models.TextField(max_length=500)
      location = models.CharField(max_length=50)
      address = models.URLField(max_length=200)
      image = models.ImageField(upload_to= 'images')
      organizer_email = models.EmailField(max_length=254)
      date = models.DateField(auto_now=False, auto_now_add=False,default = 2024-3-30)
      participants  = models.ManyToManyField(Participant,blank= True,null= True)
      

      # we can give this variables in admin.py to display the variables instead of object
      # def __str__(self):
      #       return f'{self.title} - {self.slug}'
      # to display models Meetup variable values in admin page instead of object1 ,2 we can return like above __STR__

# images need to add in settings.py at last
# MEDIA_ROOT = BASE_DIR / 'uploads'
# MEDIA_URL = '/files/'
# connecting all the Meetup variables in HTML files to display the output.      




