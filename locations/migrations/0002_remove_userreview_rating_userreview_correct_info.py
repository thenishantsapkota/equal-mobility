# Generated by Django 4.2.2 on 2023-06-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userreview",
            name="rating",
        ),
        migrations.AddField(
            model_name="userreview",
            name="correct_info",
            field=models.BooleanField(default=True),
        ),
    ]
