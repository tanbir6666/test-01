# Generated by Django 3.1.3 on 2021-03-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='text_massage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=200)),
                ('MASSAGE', models.CharField(max_length=10000)),
            ],
        ),
    ]
