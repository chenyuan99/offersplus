# Generated by Django 3.1.7 on 2023-03-20 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracks', '0005_auto_20230320_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationrecord',
            name='applicant',
            field=models.ForeignKey(default='cyuan8', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
