# Generated by Django 3.1.7 on 2022-01-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_auto_20220105_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='screenshot',
            field=models.ImageField(null=True, upload_to='screenshot'),
        ),
    ]
