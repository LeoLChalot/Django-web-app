from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

# * Import du modèle Band
from listings.models import Band
from listings.models import Listing

from listings.forms import *


def home(request):
    return render(request, 'listings/home.html')

#  ************************************ #
#  ***        Views Listings        *** #
#  ************************************ #
def listings_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings_list.html', context={'listings': listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html', {'listing': listing})


def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
        else:
            form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
        else:
            form = BandForm()
    return render(request, 'listings/listing_update.html', {'form': form})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        listing.delete()
        messages.success(request, "Groupe supprimé avec succès !")
        return redirect('listings-list')
    return render(request, 'listings/band_delete.html', {'listing': listing})


#  ************************************ #
#  ***          Views Band          *** #
#  ************************************ #
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})


def band_create(request):
    form = BandForm()
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            messages.success(request, "Groupe ajouté avec succès !")
            return redirect('band-detail', band.id)
        else:
            form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    form = BandForm(instance=band)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            messages.success(request, "Groupe modifié avec succès !")
            return redirect('band-detail', band.id)
        else:
            form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        messages.success(request, "Groupe supprimé avec succès !")
        return redirect('bands-list')
    return render(request, 'listings/band_delete.html', {'band': band})

#  ************************************ #
#  ***         Views Others         *** #
#  ************************************ #

def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form', message=form.cleaned_data['message'], from_email=form.cleaned_data['email'], recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_confirmation.html')


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})
