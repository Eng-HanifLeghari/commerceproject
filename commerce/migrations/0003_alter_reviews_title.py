# Generated by Django 3.2.8 on 2021-11-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_reviews_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='title',
            field=models.EmailField(max_length=254),
        ),
    ]
