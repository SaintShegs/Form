# Generated by Django 4.0.4 on 2022-04-11 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Applicant name')),
                ('address', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=15, verbose_name='Zip code')),
                ('phone', models.CharField(max_length=11, verbose_name='Contact Phone')),
                ('DateOfBirth', models.DateField(default=datetime.date.today)),
                ('web', models.URLField(blank=True, verbose_name='Website address')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, verbose_name='Gender')),
                ('email_address', models.EmailField(blank=True, max_length=254, verbose_name='Email address')),
                ('paid', models.BooleanField(default=False)),
                ('RegDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
