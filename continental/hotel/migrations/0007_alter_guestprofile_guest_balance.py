# Generated by Django 5.0.3 on 2024-04-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestprofile',
            name='guest_balance',
            field=models.IntegerField(default=1000),
        ),
    ]