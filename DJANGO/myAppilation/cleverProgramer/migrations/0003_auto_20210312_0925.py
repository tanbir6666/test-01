# Generated by Django 3.1.7 on 2021-03-12 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleverProgramer', '0002_userdatabase_useremail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchdata',
            options={'verbose_name_plural': 'SearchData'},
        ),
        migrations.AlterModelOptions(
            name='searchhistory',
            options={'verbose_name_plural': 'SearchHistory'},
        ),
        migrations.AlterModelOptions(
            name='userdatabase',
            options={'verbose_name_plural': 'USERS'},
        ),
    ]
