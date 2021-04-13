from rest_framework import serializers
from user_admin.models import RequestForCancelPlan, AddLicense, ReduceLicense


class RequestForCancelPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequestForCancelPlan
        fields=("RequestNo",'NoOfUsers','EffectiveDate','PlanName','ExpiryDate')

class AddLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddLicense
        fields=('Date','RequestNo','PlanName','TotalUsers','AddUsers','LicensesAfter','EffectiveDate','ActiveFlag')

class ReduceLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReduceLicense
        fields=('Date','RequestNo','PlanName','TotalUsers','ReduceUsers','LicensesAfter','EffectiveDate','ActiveFlag')



class AddLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddLicense
        fields=('Date','RequestNo','PlanName','TotalUsers','AddUsers','LicensesAfter','EffectiveDate','ActiveFlag')

class ReduceLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReduceLicense
        fields=('Date','RequestNo','PlanName','TotalUsers','ReduceUsers','LicensesAfter','EffectiveDate','ActiveFlag')
