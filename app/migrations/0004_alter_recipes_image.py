# Generated by Django 3.2 on 2021-04-30 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default=datetime.datetime(2021, 4, 30, 15, 12, 31, 947983, tzinfo=utc), upload_to='picture/'),
        ),
    ]
