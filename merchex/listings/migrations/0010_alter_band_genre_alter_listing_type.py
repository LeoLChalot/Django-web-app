# Generated by Django 4.2.1 on 2023-05-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_band_genre_alter_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')], default='HH', max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Poster'), ('M', 'Miscellaneous')], default='M', max_length=50),
        ),
    ]