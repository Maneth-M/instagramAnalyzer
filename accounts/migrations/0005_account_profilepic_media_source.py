# Generated by Django 4.0.3 on 2022-03-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_media_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profilePic',
            field=models.URLField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='media',
            name='source',
            field=models.URLField(default=' ', max_length=1000),
        ),
    ]