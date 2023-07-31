# Generated by Django 2.1.5 on 2023-03-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_auto_20230318_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='user',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user_email',
            field=models.EmailField(default='student@gmail.com', max_length=254, verbose_name='user email address'),
        ),
    ]
