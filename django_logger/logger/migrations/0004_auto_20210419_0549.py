# Generated by Django 3.0.5 on 2021-04-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20210419_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggerfile',
            name='referer_from',
            field=models.TextField(blank=True, null=True, verbose_name='referer'),
        ),
    ]
