# Generated by Django 4.2.5 on 2023-09-25 22:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_images', '0020_remove_expirelink_expiration_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='expirelink',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expirelink',
            name='expire_link_duration',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(30000)]),
        ),
    ]