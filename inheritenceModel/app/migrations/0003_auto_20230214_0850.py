# Generated by Django 3.2.12 on 2023-02-14 08:50

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_student_age'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
                ('teachers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher'),
        ),
    ]