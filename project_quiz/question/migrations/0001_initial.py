# Generated by Django 4.2.4 on 2023-08-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=10000)),
                ('alt_a', models.CharField(max_length=100)),
                ('alt_b', models.CharField(max_length=100)),
                ('alt_c', models.CharField(max_length=100)),
                ('alt_d', models.CharField(max_length=100)),
                ('resp', models.CharField(max_length=100)),
            ],
        ),
    ]
