# Generated by Django 4.0.3 on 2022-03-08 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('followers', models.JSONField(default=dict)),
                ('following', models.JSONField(default=dict)),
                ('medias', models.JSONField(default=dict)),
                ('avLikes', models.IntegerField(default=0)),
                ('avComments', models.IntegerField(default=0)),
                ('avViews', models.IntegerField(default=0)),
                ('rankLikes', models.IntegerField(default=0)),
                ('rankComments', models.IntegerField(default=0)),
                ('rankViews', models.IntegerField(default=0)),
                ('isVerified', models.BooleanField(default=False)),
                ('bio', models.TextField(default=' ')),
                ('hashtags', models.TextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('mediaId', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('caption', models.TextField(default=' ')),
                ('hashtags', models.TextField(default=' ')),
                ('datePosted', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
