# Generated by Django 4.1 on 2022-08-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
