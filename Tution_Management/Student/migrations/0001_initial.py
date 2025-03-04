# Generated by Django 5.0.3 on 2024-07-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_models',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('student_age', models.IntegerField()),
                ('student_gender', models.CharField(max_length=10)),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
