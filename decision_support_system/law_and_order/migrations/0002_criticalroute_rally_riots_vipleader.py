# Generated by Django 3.0 on 2019-12-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_and_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriticalRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime', models.TextField()),
                ('congestion', models.TextField()),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'critical_route',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('political_leader', models.CharField(max_length=255)),
                ('protest', models.TextField()),
                ('religion', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rally',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Riots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regional_party', models.CharField(max_length=255)),
                ('religion', models.CharField(max_length=255)),
                ('community_caste', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'riots',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VipLeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_leader', models.CharField(max_length=255)),
                ('religion_leader', models.CharField(max_length=255)),
                ('administrative_leader', models.CharField(max_length=255)),
                ('famous_personality', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vip_leader',
                'managed': False,
            },
        ),
    ]
