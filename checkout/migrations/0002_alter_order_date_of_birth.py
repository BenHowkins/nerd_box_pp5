# Generated by Django 3.2.24 on 2024-05-27 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]