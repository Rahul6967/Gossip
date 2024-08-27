# Generated by Django 4.2.14 on 2024-08-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_friendshiprequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('accapted', 'Accepted'), ('sent', 'Sent')], default='sent', max_length=20),
        ),
    ]
