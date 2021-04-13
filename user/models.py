from django.db import models
from django.db.models import CharField, DateField, BooleanField, IntegerField, FloatField, DecimalField, DurationField, \
    NullBooleanField,DateTimeField

# Create your models here.




class UserMaster(models.Model):
    SubscriberId=IntegerField(primary_key=True)
    UserId_email=CharField(max_length=200)
    UserName=CharField(max_length=200)
    Password=CharField(max_length=8)
    PasswordDt=DateField(max_length=8,auto_now=True)
    Role=CharField(max_length=200)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=1)
    PlanID=IntegerField()

    class Meta:
        db_table="UserMaster"

    def __str__(self):
        return str(self.SubscriberId)


class MyJobDescription(models.Model):
    JobCategory=CharField(max_length=150)
    JobTitle=CharField(max_length=150)
    JobRequirements=CharField(max_length=150)
    JobResponsibility=CharField(max_length=150)
    Perks=CharField(max_length=150)
    Skills=CharField(max_length=150)
    Qualification=CharField(max_length=150)
    Experience=CharField(max_length=150)
    CompanyName=CharField(max_length=150)
    ReportTo=CharField(max_length=150)
    City=CharField(max_length=150)
    State=CharField(max_length=150)
    Country=CharField(max_length=150)
    TimeZone=CharField(max_length=150)
    MyJobDescriptionNo=IntegerField(primary_key=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="MyJobDescription"

    def __str__(self):
        return str(self.MyJobDescriptionNo)



class JobPosting(models.Model):
    JobpostingNo=IntegerField(primary_key=True)
    JobPostingDate=DateField(max_length=8,auto_now=True)
    SubscriptionId=IntegerField()
    CustomerId=IntegerField()
    PlanID=IntegerField()
    PlanType=CharField(max_length=150)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=150)
    ModifiedBy=CharField(max_length=150)

    class Meta:
        db_table="JobPosting"

    def __str__(self):
        return str(self.JobpostingNo)

