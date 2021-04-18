"""prjapr5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

import appapr5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appapr5/', include('appapr5.urls')),
    path('registration/', include('registration.urls')),
    path('', include('home.urls')),
    path('upload/', include('profile_maker.urls')),
    #ajax
    path('ajax/', include('post.urls')),

]




# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic.base import RedirectView
# from .views import *
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('redirect/', data_flair),
#     path('dataflair/', index),
#     #path('djangotutor/', tutorial.as_view()),
#     path('ggl/', RedirectView.as_view(url ='https://google.com')),
# ]