# Generated by Django 3.1 on 2020-10-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_paper', '0008_auto_20201018_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_ans',
            field=models.JSONField(default=[], null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.JSONField(default={}, null=True),
        ),
    ]