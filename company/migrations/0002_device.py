# Generated by Django 3.1.1 on 2020-09-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_item', models.AutoField(primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=30)),
                ('device_model', models.CharField(max_length=256)),
                ('production_date', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('device_photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
