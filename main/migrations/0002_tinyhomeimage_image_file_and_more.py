# Generated by Django 5.2.4 on 2025-07-30 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tinyhomeimage',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='tiny_homes/'),
        ),
        migrations.AlterField(
            model_name='tinyhomeimage',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
