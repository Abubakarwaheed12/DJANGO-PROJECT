# Generated by Django 4.1.5 on 2023-01-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=170)),
                ('desc', models.CharField(max_length=3000)),
            ],
        ),
    ]
