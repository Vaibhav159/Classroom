# Generated by Django 3.1 on 2020-10-17 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_paper', '0002_auto_20201017_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.CharField(choices=[('THEORY', 'THEORY'), ('MCQ', 'MCQ'), ('ODD,', 'OUT one out')], default='MCQ', max_length=200),
        ),
    ]
