# Generated by Django 2.1.1 on 2018-10-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0010_auto_20181020_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
