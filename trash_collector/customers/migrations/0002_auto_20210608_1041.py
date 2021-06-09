# Generated by Django 3.1.8 on 2021-06-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pickup_day',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_start',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]