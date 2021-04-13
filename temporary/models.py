from django.db import models

# Create your models here.

from django.db.models import CharField, DateField, BooleanField, IntegerField, FloatField, DecimalField, DurationField, \
    NullBooleanField,DateTimeField



#SalesLead,
"""
JobCategory,
JobTitle,
JobResponsibility,
JobRequirement,
JobBrief,
Qualification,
Skill,
Perks,
Plan,
"""

#_________________________________________________________________________________________________________



"""
JobCategory,
JobTitle,
JobResponsibility,
JobRequirement,
JobBrief,
Qualification,
Skill,
Perks,
Plan,
Invoice,
Payment,
JobInterviewQuestion,
TranJobBrief,

"""

class TranJobBrief(models.Model):
    TransJobBriefId=IntegerField(primary_key=True)
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobBriefDescription=CharField(max_length=200)

    class Meta:
        db_table="TranJobBrief"

    def __str__(self):
        return self.TranJobBriefId

class TranJobRoles(models.Model):
    TransJobRolesID=IntegerField()
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobRolesDescription=CharField(max_length=200)

    class Meta:
        db_table="TransJobRoles"

    def __str__(self):
        return self.TransJobRolesID

class TranJobPerks(models.Model):
    TransJobPerksId=IntegerField()
    TransJDId=IntegerField()
    SubscriptionId=IntegerField()
    TransJobPerksDescription=CharField(max_length=200)

    class Meta:
        db_table="TranJobPerks"

    def __str__(self):
        return self.TransJobPerksId

class TranJobJD(models.Model):
    TransJDId=CharField(max_length=100)#models.ForeignKey()#to_fields="TransJobBriefId",)#IntegerField(primary_key=True)
    TransJDDate=DateField()
    SubscriptionId=IntegerField()
    ClientId=IntegerField()
    JdCategoryId=IntegerField()
    JdJobBriefId=IntegerField()
    JdJobTitleId=IntegerField()
    JdJobRequirementId=IntegerField()
    JdJobRolesId=IntegerField()
    JdJobPerks=CharField(max_length=200)
    Education=CharField(max_length=200)
    JDJobSkillId=IntegerField()
    JDSkillImportance=CharField(max_length=200)
    MinExperience=FloatField()
    Compensation=FloatField()
    Salary=FloatField()
    WorkLocation=CharField(max_length=200)
    TimeZone=DateTimeField()
    JDTemplateId=IntegerField()
    JDContent=CharField(max_length=300)
    JDCreatedBy=CharField(max_length=200)
    JDCreatedDate=DateField()
    JDModifiedBy=CharField(max_length=200)
    JDModifiedDate=DateField()

    class Meta:
        db_table = "TranJobJD"

    def __str__(self):
        return self.TransJDId


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#24-03-2021 api's

"""
07-04-2021
"""

class AddOrCancelRequest(models.Model):
    RequestId=IntegerField(primary_key=True)
    RequestDate=DateField(max_length=8,auto_now=True)
    SubscriptionID=IntegerField()
    CustomerId=IntegerField()
    PlanId=IntegerField()
    ExistingUser=CharField(max_length=150)
    AddReduceuser=CharField(max_length=150)
    AfterNoofUsers=IntegerField()
    InvoicegeneratedFlg=BooleanField(default=True)
    InvoiceNo=IntegerField()
    PaymentId=IntegerField()
    MailSentFlg=BooleanField(default=True)
    PaymentDoneFlg=BooleanField(default=True)
    ActivatedFlg=BooleanField(default=True)
    ActivatedDate=DateField(max_length=8,auto_now=True)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=150)
    ModifiedBy=CharField(max_length=150)


    class Meta:
        db_table="AddOrCancelRequest"

    def __str__(self):
        return str(self.RequestId)

class Tickets(models.Model):
    DateTime=DateTimeField()
    TicketNo=IntegerField()
    TicketSubject=CharField(max_length=150)
    TicketStatus=BooleanField()
    DateOfCompletion=DateField(max_length=8,auto_now=True)

    class Meta:
        db_table="Tickets"

    def __str__(self):
        return str(self.TicketNo)

    