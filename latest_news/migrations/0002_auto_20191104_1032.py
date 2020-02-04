# Generated by Django 2.2.6 on 2019-11-04 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('latest_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest_news',
            name='news_dt',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 10, 32, 3, 674158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 10, 32, 3, 674582, tzinfo=utc)),
        ),
    ]
