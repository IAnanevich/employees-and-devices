# Generated by Django 3.1.1 on 2020-09-26 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_device_device_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('delivery_date', models.DateField(auto_now=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='company.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.employees')),
            ],
        ),
    ]
