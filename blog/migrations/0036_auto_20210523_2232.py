# Generated by Django 3.1.6 on 2021-05-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20210515_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
