# Generated by Django 4.2.14 on 2024-08-17 03:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_friendshiprequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='people_you_may_know',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('sent', 'Sent'), ('accapted', 'Accepted')], default='sent', max_length=20),
        ),
    ]
