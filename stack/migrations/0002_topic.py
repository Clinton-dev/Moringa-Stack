# Generated by Django 4.0.5 on 2022-06-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
