# Generated by Django 3.1.3 on 2020-12-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201127_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ssn',
            field=models.TextField(default=''),
        ),
    ]
