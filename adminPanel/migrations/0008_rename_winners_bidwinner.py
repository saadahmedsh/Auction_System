# Generated by Django 3.2.5 on 2021-08-09 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0007_winners'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='winners',
            new_name='bidWinner',
        ),
    ]
