# Generated by Django 2.0 on 2018-05-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='controller_name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
