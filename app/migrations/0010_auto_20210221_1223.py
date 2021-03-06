# Generated by Django 3.1.7 on 2021-02-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_business_refferal_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='busi_grp',
            field=models.CharField(choices=[('Business_Partner', 'Business_Partner')], default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='refferal',
            name='ref_grp',
            field=models.CharField(choices=[('Referral', 'Referral')], default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='candi_grp',
            field=models.CharField(choices=[('Candidate', 'Candidate')], default=None, max_length=50),
        ),
    ]
