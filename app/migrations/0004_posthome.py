# Generated by Django 3.1.1 on 2021-02-16 07:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210213_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_homeImage', models.ImageField(upload_to='images/')),
                ('banner_AboutImage', models.ImageField(upload_to='images/')),
                ('banner_Aboutcarousel_image', models.ImageField(upload_to='images/')),
                ('banner_review_image', models.ImageField(upload_to='images/')),
                ('About_heading', models.CharField(max_length=50)),
                ('Vision_heading', models.CharField(max_length=50)),
                ('Service_heading', models.CharField(max_length=50)),
                ('About_body', ckeditor.fields.RichTextField()),
                ('Vision_body', ckeditor.fields.RichTextField()),
                ('Service_body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
