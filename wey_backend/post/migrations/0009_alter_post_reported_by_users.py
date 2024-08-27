# Generated by Django 4.2.14 on 2024-08-21 05:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0008_post_reported_by_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reported_by_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
