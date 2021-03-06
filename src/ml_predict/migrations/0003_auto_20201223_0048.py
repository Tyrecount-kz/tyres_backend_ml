# Generated by Django 2.2 on 2020-12-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_predict', '0002_auto_20201223_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='company',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='custom_cleared',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='gear',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='mileage',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='model',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='rudder',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='shell',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='transmisson',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='type_engine',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='volume',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]
