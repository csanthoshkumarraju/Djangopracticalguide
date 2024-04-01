"""
URL configuration for django_course_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# Link the paths from app urls.py in this folder.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('meetups.urls')) # path/include Need to give app urls.py folder dicrectory/path
] +  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# ****************************************************************
# Linking the path files
# ****************************************************************

# 1) views.py contains functions and classes in the app folder.
# 2) app urls.py contains the app path
# 3) Project urls.py contains the project path, which is the main

# We need to link app views.py file --> app urls.py file -> project urls.py
# static is used to serve uploaded pics. so, we are importing settings.py and usong in static.


 