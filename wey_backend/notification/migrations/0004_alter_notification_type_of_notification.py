# Generated by Django 4.2.14 on 2024-08-17 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type_of_notification',
            field=models.CharField(choices=[('new_friendrequest', 'New Friendrequest'), ('accepted_friendrequest', 'Accepted Friendrequest'), ('rejected_friendrequest', 'Rejected Friendrequest'), ('post_like', 'Post Like'), ('post_comment', 'Post Comment')], max_length=50),
        ),
    ]
