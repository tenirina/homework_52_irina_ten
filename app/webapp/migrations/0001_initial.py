# Generated by Django 4.1.1 on 2022-09-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Description')),
                ('status', models.CharField(default='New', max_length=50, verbose_name='Status')),
                ('completion_data', models.DateField(default=None, null=True, verbose_name='Date of completion')),
            ],
        ),
    ]
