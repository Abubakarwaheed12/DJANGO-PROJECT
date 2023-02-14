# Generated by Django 4.1.6 on 2023-02-13 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('grade', models.IntegerField(default=14)),
                ('subject', models.CharField(choices=[('English', 'English'), ('Math', 'Math'), ('Physics', 'Physics'), ('Zology', 'Zology'), ('Computer', 'Computer')], max_length=50)),
                ('is_hod', models.BooleanField(default=False)),
                ('headOfDepartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teachers')),
            ],
        ),
    ]