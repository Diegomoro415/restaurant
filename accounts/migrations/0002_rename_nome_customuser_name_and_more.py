# Generated by Django 4.2.3 on 2023-08-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='telefone',
            new_name='phone',
        ),
    ]