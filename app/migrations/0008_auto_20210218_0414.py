# Generated by Django 3.1.1 on 2021-02-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210218_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage6',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage7',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]