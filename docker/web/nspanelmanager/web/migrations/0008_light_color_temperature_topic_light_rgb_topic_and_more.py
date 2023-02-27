# Generated by Django 4.1.7 on 2023-02-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_room_displayorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='color_temperature_topic',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='light',
            name='rgb_topic',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='light',
            name='cmd_topic',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='light',
            name='state_topic',
            field=models.CharField(default='', max_length=255),
        ),
    ]