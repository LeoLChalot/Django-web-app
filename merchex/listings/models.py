from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# listings/models.py


class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        METAL = 'M'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(
        choices=Genre.choices, max_length=50, default='HH')
    biography = models.fields.CharField(
        max_length=1000, default='', blank=True)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTER = 'P'
        MISCELLANEOUS = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100, default='')
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(
        choices=Type.choices, max_length=50, default='M')
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
