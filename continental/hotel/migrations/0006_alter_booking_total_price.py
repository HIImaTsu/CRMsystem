# Generated by Django 5.0.3 on 2024-04-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_remove_guest_country_guestprofile_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
        ),
    ]