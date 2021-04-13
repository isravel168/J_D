# Generated by Django 3.0.4 on 2021-04-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('JobpostingNo', models.IntegerField(primary_key=True, serialize=False)),
                ('JobPostingDate', models.DateField(auto_now=True, max_length=8)),
                ('SubscriptionId', models.IntegerField()),
                ('CustomerId', models.IntegerField()),
                ('PlanID', models.IntegerField()),
                ('PlanType', models.CharField(max_length=150)),
                ('CreatedDate', models.DateField(auto_now=True, max_length=8)),
                ('ModifiedDate', models.DateField(auto_now=True, max_length=8)),
                ('CreatedBy', models.CharField(max_length=150)),
                ('ModifiedBy', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'JobPosting',
            },
        ),
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
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('SubscriberId', models.IntegerField(primary_key=True, serialize=False)),
                ('UserId_email', models.CharField(max_length=200)),
                ('UserName', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=8)),
                ('PasswordDt', models.DateField(auto_now=True, max_length=8)),
                ('Role', models.CharField(max_length=200)),
                ('CreatedBy', models.CharField(max_length=200)),
                ('CreatedDate', models.DateField(auto_now=True, max_length=8)),
                ('ModifiedBy', models.CharField(max_length=200)),
                ('ModifiedDate', models.DateField(auto_now=True, max_length=8)),
                ('ActiveFlag', models.BooleanField(default=1)),
                ('PlanID', models.IntegerField()),
            ],
            options={
                'db_table': 'UserMaster',
            },
        ),
    ]
