# Generated by Django 4.2.2 on 2023-07-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img',
            field=models.ImageField(upload_to='picss'),
        ),
    ]
