# Generated by Django 3.1.6 on 2021-05-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0015_auto_20210523_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduct',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]