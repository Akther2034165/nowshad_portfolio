# Generated by Django 5.0.3 on 2024-03-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
