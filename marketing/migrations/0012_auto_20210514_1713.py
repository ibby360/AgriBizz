# Generated by Django 3.1.6 on 2021-05-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0011_remove_postproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduct',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='thumbnail',
            field=models.ImageField(default='No-Image-Placeholder.svg', upload_to='static/img/'),
        ),
    ]
