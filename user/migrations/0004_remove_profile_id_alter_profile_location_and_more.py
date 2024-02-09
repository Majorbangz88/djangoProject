# Generated by Django 5.0.2 on 2024-02-08 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tweeter_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
