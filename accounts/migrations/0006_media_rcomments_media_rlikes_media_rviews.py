# Generated by Django 4.0.3 on 2022-03-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_profilepic_media_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='rComments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='media',
            name='rLikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='media',
            name='rViews',
            field=models.IntegerField(default=0),
        ),
    ]
