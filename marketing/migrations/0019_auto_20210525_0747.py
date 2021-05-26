# Generated by Django 3.1.6 on 2021-05-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0018_auto_20210524_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postproduct',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='postproduct',
            old_name='scale',
            new_name='unit',
        ),
        migrations.RemoveField(
            model_name='postproduct',
            name='full_name',
        ),
        migrations.AddField(
            model_name='postproduct',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='postproduct',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='postproduct',
            name='middle_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]