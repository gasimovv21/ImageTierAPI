# Generated by Django 4.2.5 on 2023-09-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_images', '0022_userimage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='expirelink',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
