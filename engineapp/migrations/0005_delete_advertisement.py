# Generated by Django 5.1.3 on 2024-11-15 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineapp', '0004_advertisement_delete_ad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advertisement',
        ),
    ]