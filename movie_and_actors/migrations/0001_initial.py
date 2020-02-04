# Generated by Django 2.2.6 on 2019-11-04 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmstars', '0001_initial'),
        ('latest_news', '0001_initial'),
        ('movie_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_and_actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmstars.filmstars')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='latest_news.latest_news')),
            ],
        ),
        migrations.CreateModel(
            name='movie_and_actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmstars.filmstars')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_details.movie_details')),
            ],
        ),
    ]