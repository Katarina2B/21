# Generated by Django 2.0.3 on 2018-11-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20181117_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='platter',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sub',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sub',
            name='size',
            field=models.CharField(max_length=50),
        ),
    ]
