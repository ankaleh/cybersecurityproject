# Generated by Django 3.1.3 on 2020-11-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(),
        ),
    ]