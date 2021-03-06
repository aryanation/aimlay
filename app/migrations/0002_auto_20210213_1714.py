# Generated by Django 3.1.1 on 2021-02-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='timezone.now', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='message',
            field=models.TextField(default='-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='target',
            field=models.CharField(choices=[('C', 'Candidate'), ('R', 'Referral'), ('BP', 'Business_Partner')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
