# Generated by Django 3.1.1 on 2020-09-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='RCWorld', max_length=255),
        ),
    ]
