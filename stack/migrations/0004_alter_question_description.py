# Generated by Django 4.0.5 on 2022-06-20 08:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]