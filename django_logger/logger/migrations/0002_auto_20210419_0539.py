# Generated by Django 3.0.5 on 2021-04-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggerfile',
            name='uri',
            field=models.CharField(max_length=500, verbose_name='uri'),
        ),
    ]