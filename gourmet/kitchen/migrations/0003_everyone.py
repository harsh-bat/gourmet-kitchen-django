# Generated by Django 2.1.1 on 2018-09-30 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('kitchen', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Everyone',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('about', models.CharField(max_length=5000, null=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('dp', models.FileField(upload_to='kitchen/dp')),
                ('cover', models.FileField(upload_to='kitchen/cover')),
                ('type', models.CharField(max_length=1)),
            ],
        ),
    ]
