# Generated by Django 4.2.14 on 2024-08-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_people_you_may_know_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('accapted', 'Accepted'), ('rejected', 'Rejected')], default='sent', max_length=20),
        ),
    ]
