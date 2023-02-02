# Generated by Django 4.1.5 on 2023-01-13 14:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_certificate_cert"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="certificate",
            options={
                "ordering": ["name"],
                "verbose_name": "Certificate",
                "verbose_name_plural": "Certificates",
            },
        ),
        migrations.AddField(
            model_name="certificate",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
