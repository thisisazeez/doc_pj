# Generated by Django 4.0 on 2022-01-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_students_country_students_nxt_kin_num_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fee_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
