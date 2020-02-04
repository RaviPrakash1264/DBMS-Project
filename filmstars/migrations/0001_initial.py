# Generated by Django 2.2.6 on 2019-11-04 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filmstars',
            fields=[
                ('actor_name', models.CharField(max_length=80, unique=True)),
                ('actor_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('date_of_birth', models.DateField(max_length=8)),
                ('died', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(max_length=1)),
                ('years_active', models.IntegerField()),
                ('actor_image', models.ImageField(upload_to='')),
                ('synopsis', models.TextField(max_length=30)),
            ],
        ),
    ]