# Generated by Django 4.1.5 on 2023-01-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_contactprofile_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactprofile",
            name="message",
            field=models.TextField(verbose_name="Message"),
        ),
    ]
