# Generated by Django 4.2.14 on 2024-08-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_friends_friendshiprequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends_count',
            field=models.IntegerField(default=0),
        ),
    ]
