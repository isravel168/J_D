# Generated by Django 3.0.4 on 2021-04-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporary', '0002_addlicense_cancellationplan_reducelicense_requestforcancelplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyJobDescription',
            fields=[
                ('JobCategory', models.CharField(max_length=150)),
                ('JobTitle', models.CharField(max_length=150)),
                ('JobRequirements', models.CharField(max_length=150)),
                ('JobResponsibility', models.CharField(max_length=150)),
                ('Perks', models.CharField(max_length=150)),
                ('Skills', models.CharField(max_length=150)),
                ('Qualification', models.CharField(max_length=150)),
                ('Experience', models.CharField(max_length=150)),
                ('CompanyName', models.CharField(max_length=150)),
                ('ReportTo', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Country', models.CharField(max_length=150)),
                ('TimeZone', models.CharField(max_length=150)),
                ('MyJobDescriptionNo', models.IntegerField(primary_key=True, serialize=False)),
                ('ActiveFlag', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'MyJobDescription',
            },
        ),
    ]
