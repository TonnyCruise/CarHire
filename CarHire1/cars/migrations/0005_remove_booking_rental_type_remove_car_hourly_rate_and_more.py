# Generated by Django 5.1.7 on 2025-04-01 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_booking_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='rental_type',
        ),
        migrations.RemoveField(
            model_name='car',
            name='hourly_rate',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
