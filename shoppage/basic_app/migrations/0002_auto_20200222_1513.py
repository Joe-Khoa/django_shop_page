# Generated by Django 3.0.3 on 2020-02-22 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billdetail',
            options={'get_latest_by': ['id'], 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bills',
            options={'get_latest_by': ['id'], 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'get_latest_by': ['id'], 'managed': False},
        ),
    ]
