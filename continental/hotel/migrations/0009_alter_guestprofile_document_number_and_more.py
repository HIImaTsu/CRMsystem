# Generated by Django 5.0.3 on 2024-04-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_booking_time_create_booking_time_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestprofile',
            name='document_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guestprofile',
            name='iin',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]