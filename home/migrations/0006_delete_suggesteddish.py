# Generated by Django 4.2.3 on 2023-08-12 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userreview_approved_userreview_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SuggestedDish',
        ),
    ]
