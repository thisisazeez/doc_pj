# Generated by Django 4.0 on 2022-01-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_staffdepartments_remove_staffs_customer_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cons',
            name='is_not_approved',
            field=models.BooleanField(default=False),
        ),
    ]
