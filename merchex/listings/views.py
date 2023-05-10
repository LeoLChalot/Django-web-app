from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

# * Import du modèle Band
from listings.models import Band
from listings.models import Listing

from listings.forms import *

def home(request):
        return render(request, 'listings/home.html')

def listings_list(request):
        listings = Listing.objects.all()
        return render(request,
                'listings/listings_list.html',
                context={'listings': listings})

def listing_detail(request, id):
        listing = Listing.objects.get(id=id)
        return render(request,
                'listings/listing_detail.html',
                { 'listing': listing })

def listing_create(request):
        form = ListingForm()
        if request.method == 'POST':
                form = ListingForm(request.POST)
                if form.is_valid():
                        listing = form.save()
                        return redirect('listing-detail', listing.id)
                else:
                        form = ListingForm()
        return render(request,'listings/listing_create.html', {'form': form})

def contact(request):
        # print('Lam éthode de requête est : ', request.method)
        # print('Les données POST sont : ', request.POST)
        if request.method == 'POST':
                form = ContactUsForm(request.POST)
                if form.is_valid():
                        send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form', message=form.cleaned_data['message'], from_email=form.cleaned_data['email'], recipient_list=['admin@merchex.xyz'],
                        )
                        return redirect('email-sent')
        else:
                form = ContactUsForm()

        return render(request, 'listings/contact.html', {'form':form})

def email_sent(request):
        return render(request, 'listings/email_confirmation.html')

def band_list(request):
        bands = Band.objects.all()
        return render(request,
                'listings/band_list.html',
                context={'bands': bands})

def band_detail(request, id):
        band = Band.objects.get(id=id)
        return render(request,
                'listings/band_detail.html',
                { 'band': band })

def band_create(request):
        form = BandForm()
        if request.method == 'POST':
                form = BandForm(request.POST)
                if form.is_valid():
                        band = form.save()
                        return redirect('band-detail', band.id)
                else:
                        form =BandForm()
        return render(request, 'listings/band_create.html', {'form':form})

def about(request):
        return render(request, 'listings/about.html')
