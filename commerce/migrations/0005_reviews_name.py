# Generated by Django 3.2.8 on 2021-11-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_alter_reviews_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
