from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style':'width:300px', 'class':'form-control'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style':'width:300px', 'class':'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'style':'width:300px', 'class':'form-control'}),max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'