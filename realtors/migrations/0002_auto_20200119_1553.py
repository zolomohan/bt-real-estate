# Generated by Django 3.0.2 on 2020-01-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]