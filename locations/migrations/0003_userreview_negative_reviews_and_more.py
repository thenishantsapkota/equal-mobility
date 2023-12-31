# Generated by Django 4.2.2 on 2023-06-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0002_remove_userreview_rating_userreview_correct_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="userreview",
            name="negative_reviews",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userreview",
            name="positive_reviews",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
