# Generated by Django 4.2.1 on 2023-05-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_band_genre_alter_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('M', 'Metal')], default='HH', max_length=50),
        ),
    ]
