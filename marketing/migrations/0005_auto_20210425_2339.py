# Generated by Django 3.1.6 on 2021-04-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20210425_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduct',
            name='scale',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Debe', 'Debe'), ('Sack', 'Sack'), ('Tons', 'Tons')], default='Kg', max_length=50),
        ),
    ]