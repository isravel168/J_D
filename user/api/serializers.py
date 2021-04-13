from rest_framework import  serializers
from ..models import MyJobDescription, JobPosting, UserMaster


class UserMasterSerializer(serializers.ModelSerializer):
    model=UserMaster
    fields=("SubscriberId","UserId_email","UserName","Password","PasswordDt","Role","CreatedBy","CreatedDate",\
            "ModifiedBy","ModifiedDate","ActiveFlag","PlanID")


class MyJobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyJobDescription
        fields=('JobCategory','JobTitle','JobRequirements','JobResponsibility','Perks','Skills',\
                'Qualification','Experience','CompanyName','ReportTo','City','State','Country','TimeZone','MyJobDescriptionNo',\
                'ActiveFlag')


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobPosting
        fields=('JobpostingNo', 'JobPostingDate', 'SubscriptionId', 'CustomerId', 'PlanID', 'PlanType', 'CreatedDate', 'ModifiedDate', 'CreatedBy', 'ModifiedBy')

