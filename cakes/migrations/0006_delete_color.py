# Generated by Django 5.1.2 on 2024-11-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0005_alter_cake_color_alter_cake_date_create_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color',
        ),
    ]
