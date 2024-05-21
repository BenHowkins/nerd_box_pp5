# Generated by Django 3.2.24 on 2024-05-21 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]
