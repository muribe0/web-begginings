# Generated by Django 5.0.7 on 2024-07-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(blank=True, default=500),
            preserve_default=False,
        ),
    ]
