# Generated by Django 5.0.3 on 2024-03-27 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_guests', models.IntegerField()),
                ('number_of_nights', models.IntegerField()),
                ('status_of_guest', models.CharField(choices=[('I', 'Заезжающий'), ('S', 'Проживающий'), ('O', 'Выехавший')], default='I', max_length=1)),
                ('way_of_staying', models.CharField(max_length=255)),
                ('checkin_date', models.DateTimeField()),
                ('checkout_date', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='hotel.guest')),
            ],
        ),
        migrations.CreateModel(
            name='GuestProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('document_number', models.CharField(max_length=50, unique=True)),
                ('document_date', models.DateField()),
                ('deadline_of_document', models.DateField()),
                ('guest_balance', models.IntegerField()),
                ('guest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='hotel.guest')),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guests', to='hotel.hotel'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField()),
                ('payment_method', models.CharField(choices=[('CASH', 'Наличные'), ('KASPI', 'KASPI'), ('HALYK', 'HALYK'), ('NON_CASH', 'Безналичные')], max_length=30)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='hotel.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='hotel.hotel')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rooms', to='hotel.roomtype')),
            ],
            options={
                'unique_together': {('hotel', 'room_number')},
            },
        ),
        migrations.CreateModel(
            name='HouseKeeping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('is_clean', models.BooleanField(default=False)),
                ('checkin_time', models.DateTimeField()),
                ('checkout_time', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='housekeepings', to='hotel.room')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='hotel.room'),
        ),
    ]
