# Generated by Django 4.0.4 on 2022-06-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_current_address_student_permanent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]