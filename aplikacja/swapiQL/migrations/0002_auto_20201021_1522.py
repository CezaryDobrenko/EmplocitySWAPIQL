# Generated by Django 3.1.2 on 2020-10-21 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swapiQL', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actors',
            new_name='MainCharacters',
        ),
    ]