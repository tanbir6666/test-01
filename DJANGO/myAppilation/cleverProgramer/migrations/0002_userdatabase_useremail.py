# Generated by Django 3.1.7 on 2021-03-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleverProgramer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatabase',
            name='userEmail',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]
