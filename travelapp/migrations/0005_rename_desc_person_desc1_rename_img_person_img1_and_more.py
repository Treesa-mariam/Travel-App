# Generated by Django 4.2.2 on 2023-07-03 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_alter_person_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='name1',
        ),
    ]
