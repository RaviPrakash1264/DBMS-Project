# Generated by Django 2.2.6 on 2019-11-02 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_details',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('movie_name', models.CharField(max_length=30)),
                ('imdb_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('rt_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('metacritic_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('movie_image', models.ImageField(default='', upload_to='')),
                ('genre', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('total_episodes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('synopsis', models.TextField(max_length=30)),
            ],
        ),
    ]
