from django.db import models

# Create your models here.

from django.db.models import CharField, DateField, BooleanField, IntegerField, FloatField, DecimalField, DurationField, \
    NullBooleanField,DateTimeField



class AddLicense(models.Model):
    Date=DateField(max_length=8,auto_now=True)
    RequestNo=IntegerField(primary_key=True)
    PlanName=CharField(max_length=150)
    TotalUsers=IntegerField()
    AddUsers=IntegerField()
    LicensesAfter= IntegerField()
    EffectiveDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="AddLicense"

    def __str__(self):
        return str(self.RequestNo)


class ReduceLicense(models.Model):
    Date=DateField(max_length=8,auto_now=True)
    RequestNo=IntegerField(primary_key=True)
    PlanName=CharField(max_length=150)
    TotalUsers=IntegerField()
    ReduceUsers=IntegerField()
    LicensesAfter= IntegerField()
    EffectiveDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="ReduceLicense"


    def __str__(self):
        return str(self.RequestNo)



class RequestForCancelPlan(models.Model):
    RequestNo=IntegerField(primary_key=True)
    NoOfUsers=IntegerField()
    EffectiveDate=DateField(max_length=8,auto_now=True)
    PlanName=CharField(max_length=150)
    ExpiryDate=DateField(max_length=8,auto_now=True)

    class Meta:
        db_table="RequestForCancelPlan"


    def __str__(self):
        return str(self.RequestNo)

