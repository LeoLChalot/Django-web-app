from django.http import HttpResponse
from django.shortcuts import render

# * Import du modèle Band
from listings.models import Band
from listings.models import Listing

def home(request):
        return HttpResponse('<h1>Page d\'accueil</h1>')
def listings(request):
        listings = Listing.objects.all()
        return HttpResponse(f"""
                <h1>Listings</h1>
                <p>Recencement des articles</p>
                <ul>
                        <li>{listings[0].title}</li>
                        <li>{listings[1].title}</li>
                        <li>{listings[2].title}</li>
                        <li>{listings[3].title}</li>
                </ul>
        """)
def contact(request):
        return HttpResponse('<h1>Contact</h1><p>Formulaire de contact à venir</p>')
def hello(request):
        bands = Band.objects.all()
        return HttpResponse(f"""
                <h1>Hello Django !</h1>
                <p>Mes groupes préférés sont : </p>
                <ul>
                        <li>{bands[0].name}</li>
                        <li>{bands[1].name}</li>
                        <li>{bands[2].name}</li>
                </ul>
        """)
def about(request):
        return HttpResponse('<h1>A propos</h1><p>Nous adorons Merch App !</p>')