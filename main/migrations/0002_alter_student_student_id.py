# Generated by Django 4.0.4 on 2022-06-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
