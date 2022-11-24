from django.urls import path
from .views import *

urlpatterns = [
    path('', car),
    path('index.html',home),
    path('about.html/',about),
    path('contact.html/',contact),
    path('furnitures.html/',furnitures),
    path('testimonial.html/',testimonial)
]
