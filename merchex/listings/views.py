from django.http import HttpResponse
from django.shortcuts import render

# * Import du modèle Band
from listings.models import Band
from listings.models import Listing


def home(request):
        return HttpResponse('<h1>Page d\'accueil</h1>')


def listings(request):
        listings = Listing.objects.all()
        return render(request,
                'listings/listings.html',
                context={'articles': listings})


def contact(request):
        return render(request, 'listings/contact.html')


def hello(request):
        bands = Band.objects.all()
        return render(request,
                'listings/hello.html',
                context={'bands': bands})


def about(request):
        return render(request, 'listings/about.html')
