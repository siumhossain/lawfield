# Generated by Django 3.2.8 on 2021-12-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('option_A', models.CharField(max_length=300)),
                ('option_B', models.CharField(max_length=300)),
                ('option_C', models.CharField(max_length=300)),
                ('option_D', models.CharField(max_length=300)),
                ('right_ans', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
