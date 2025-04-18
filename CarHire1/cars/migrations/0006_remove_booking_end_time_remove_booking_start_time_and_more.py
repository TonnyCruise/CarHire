# Generated by Django 5.1.7 on 2025-04-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_booking_rental_type_remove_car_hourly_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
