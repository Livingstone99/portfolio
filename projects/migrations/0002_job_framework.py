# Generated by Django 3.0.6 on 2020-05-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='framework',
            field=models.CharField(default='python development', max_length=100),
        ),
    ]
