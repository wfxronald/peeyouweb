# Generated by Django 3.0.6 on 2020-05-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_titlecard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlecard',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
