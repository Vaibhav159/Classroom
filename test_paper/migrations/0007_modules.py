# Generated by Django 3.1 on 2020-10-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_paper', '0006_auto_20201018_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleID', models.IntegerField()),
                ('questions', models.ManyToManyField(to='test_paper.Question')),
            ],
        ),
    ]
