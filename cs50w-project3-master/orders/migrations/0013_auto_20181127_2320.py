# Generated by Django 2.0.3 on 2018-11-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platter',
            name='size',
            field=models.CharField(max_length=50),
        ),
    ]
