# Generated by Django 3.1.7 on 2021-02-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210218_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businame', models.CharField(max_length=50)),
                ('busiemail', models.EmailField(max_length=254)),
                ('busimobile', models.IntegerField()),
                ('busiaddress', models.CharField(max_length=50)),
                ('busimsg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refferal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refname', models.CharField(max_length=50)),
                ('refemail', models.EmailField(max_length=254)),
                ('refmobile', models.IntegerField()),
                ('refaddress', models.CharField(max_length=50)),
                ('refmsg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stuemail', models.EmailField(max_length=254)),
                ('stumobile', models.IntegerField()),
                ('stuaddress', models.CharField(max_length=50)),
                ('stumsg', models.TextField()),
            ],
        ),
    ]
