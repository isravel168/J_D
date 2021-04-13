from django.db import models

# Create your models here.
from django.db.models import CharField, DateField, BooleanField, IntegerField, FloatField, DecimalField, DurationField, \
    NullBooleanField,DateTimeField


class Enquiry(models.Model):
    EnquiryDate=DateField(max_length=8,auto_now=True)
    EnquiryNo=IntegerField(primary_key=True)
    CustomerName=CharField(max_length=150)
    Description=CharField(max_length=150)
    NoOfUsers=IntegerField()
    LeadNo=IntegerField()
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="Enquiry"

    def __str__(self):
        return str(self.EnquiryNo)





class CustomerMaster(models.Model):
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
        db_table="CustomerMaster"

    def __str__(self):
        return str(self.SubscriberId)



class Plan(models.Model):
    PlanId=IntegerField(primary_key=True)
    PlanType=CharField(max_length=150)
    PlanName=CharField(max_length=200)
    PlanEffectiveDate=DateField(max_length=8,auto_now=True)
    NoOfDays=IntegerField()
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Plan"

    def __str__(self):
        return str(self.PlanId)



class Subscriptions(models.Model):
    SubscriptionNo=CharField(max_length=15,primary_key=True)
    SubscriptionDate=DateField(max_length=8,auto_now=True)
    EnquiryNo=CharField(max_length=15)
    CustomerID=CharField(max_length=15)
    CustomerName=CharField(max_length=200)
    PlanID=CharField(max_length=15)
    NoOfUsers=IntegerField()
    SalesOrderNo=IntegerField()
    OrderDate=DateField(max_length=8,auto_now=True)
    ActivationDate=DateField(max_length=8,auto_now=True)
    NoOfMonths=IntegerField()
    InvoicegeneratedFlg=BooleanField(default=False)
    PaymentFlg=BooleanField(default=False)
    MailSentFlg=BooleanField(default=False)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=False)

    class Meta:
        db_table="Subscriptions"

    def __str__(self):
        return str(self.SubscriptionNo)


class SalesLead(models.Model):
    SaledLeadId=CharField(max_length=15,primary_key=True)#IntegerField()
    CustomerName=CharField(max_length=200)
    CompanyIndividual=CharField(max_length=200)
    CompanyName=CharField(max_length=500)
    ContactNo=CharField(max_length=10)
    EmailId=CharField(max_length=150)
    Designation=CharField(max_length=200)
    LeadThru=CharField(max_length=200)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="SalesLead"

    def __str__(self):
        return str(self.SalesLeadId)





class Invoice(models.Model):
    InvoiceId=IntegerField(primary_key=True)
    InvoiceDate=DateField(max_length=8,auto_now=True)
    SubscriptionId=IntegerField()
    CustomerId=IntegerField()
    ActiveFlag=BooleanField()
    PlanId=IntegerField()
    InvoiceType=CharField(max_length=150)
    AdditionalUsers=CharField(max_length=200)
    UpgradePlanId=IntegerField()
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=200)
    ModifiedBy=CharField(max_length=200)

    class Meta:
        db_table="Invoice"

    def __str__(self):
        return self.InvoiceId




class Payment(models.Model):

    PaymentId=IntegerField(primary_key=True)
    PaymentDate=DateField(max_length=8,auto_now=True)
    SubscriptionCode=IntegerField()
    InvoiceNo=IntegerField()
    InvoiceType=CharField(max_length=150)
    CustomerId=IntegerField()
    SalesOrderId=IntegerField()
    PaymentMode=CharField(max_length=200)
    PaymentDate=DateField(max_length=8,auto_now=True)
    PayemntAmt=DecimalField(decimal_places=2,max_digits=10)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    CreatedBy=CharField(max_length=200)
    ModifiedBy=CharField(max_length=200)


    class Meta:
        db_table="Payment"

    def __str__(self):
        return self.PaymentId


class Qualification(models.Model):
    #primary_key=True QualificationID
    QualificationID=IntegerField()
    QualificationName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Qualification"

    def __str__(self):
        return str(self.QualificationID)



class Skill(models.Model):
    SkillID=IntegerField()
    SkillName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Skill"

    def __str__(self):
        return str(self.SkillID)


class Perks(models.Model):

    #primary_key=True Skill ID

    PerksID=IntegerField(primary_key=True)
    PerksName=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlg=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Perks"

    def __str__(self):
        return str(self.PerksID)


class CancellationPlan(models.Model):
    CancelId=IntegerField(primary_key=True)
    CustomerName=CharField(max_length=150)
    CustomerEmail=CharField(max_length=150)
    CompanyName=CharField(max_length=150)
    PlanName=CharField(max_length=150)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="CancellationPlan"

    def __str__(self):
        return str(self.CancelId)



class JobResponsibility(models.Model):
    JobRolesResponsibilityID=IntegerField(primary_key=True)
    JobTitleId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField()
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlag=BooleanField(default=0)
    CreatedBy=CharField(max_length=200)
    CreatedDate=DateField(max_length=True,auto_now=True)
    ModifiedBy=CharField(max_length=200)
    ModifiedDate=DateField(max_length=True,auto_now=True)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="JobResponsibility"

    def __str__(self):
        return str(self.JobResCatCode)



class JobRequirement(models.Model):
    JobRequirementID=CharField(max_length=15,primary_key=True)
    JobTitle=CharField(max_length=500)
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=CharField(max_length=15,default="000KDF")
    ApprovalFlag=BooleanField(default=True)
    ClientSpecificFlag=BooleanField(default=True)
    CreatedBy=CharField(max_length=200,default="kumar")
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200,default="isravel")
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="JobRequirement"

    def __str__(self):
        return str(self.JobReqCode)


class JobBrief(models.Model):
    JobBriefID=CharField(max_length=15,primary_key=True)
    JobTitleId=CharField(max_length=15)
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    SuscriberId=IntegerField(default=43)
    ApprovalFlag=BooleanField(default=0)
    ClientSpecificFlag=BooleanField(default=0)
    CreatedBy=CharField(max_length=200,default="israve")
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=200, default="kumar")
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="JobBrief"

    def __str__(self):
        return str(self.JobBrfCatCode)






class JobCategory(models.Model):
    JobCategoryId=CharField(max_length=15,primary_key=True)
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    ApprovalFlag=BooleanField(default=True)
    ClientSpecificFlag=BooleanField(default=True)
    CreatedBy=CharField(max_length=50,default="israve")
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=50,default="kumar")
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=False)

    class Meta:
        db_table="JobCategory"

    def __str__(self):
        return str(self.JobCategoryId)


class JobTitle(models.Model):
    JobTitleID=CharField(max_length=15,primary_key=True)
    JobCategory=CharField(max_length=15)
    Name=CharField(max_length=50)
    Description=CharField(max_length=500)
    SuscriberId=CharField(max_length=15,default="000KDF")
    ApprovalFlag=BooleanField(default=True)
    ClientSpecificFlag=BooleanField(default=True)
    CreatedBy=CharField(max_length=50,default="isravel")
    CreatedDate=DateField(max_length=8,auto_now=True)
    ModifiedBy=CharField(max_length=50,default="kumar")
    ModifiedDate=DateField(max_length=8,auto_now=True)
    ActiveFlag=BooleanField(default=True)

    class Meta:
        db_table="JobTitle"

    def __str__(self):
        return str(self.JobTttleCode)




class JobInterviewQuestion(models.Model):
    JobIntQuesCatCode=CharField(max_length=10)
    JobIntQuesTtlCode=CharField(max_length=10)#models.ForeignKey(to=JobTitle,on_delete=models.CASCADE)
    JobIntQuesCode=CharField(max_length=10,primary_key=True)
    JobIntQuesType=CharField(max_length=100)
    JobIntQuesDescription=CharField(max_length=250)
    JobIntQuesCreatedBy=CharField(max_length=50)
    JobIntQuesCreatedDate=DateField(max_length=8)
    JobIntQuesUpdatedBy=CharField(max_length=50)
    JobIntQuesUpdatedDate=DateField(max_length=8)
    JJobIntQuesDelFlag=BooleanField(max_length=10)

    class Meta:
        db_table="JobInterviewQuestion"

    def __str__(self):
        return self.JobIntQuesCatCode


class City(models.Model):

    #CityId is primary_key

    CityId=IntegerField(primary_key=True)#IntegerField(primary_key=True)
    StateId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    TimeZone=DateTimeField()
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="City"

    def __str__(self):
        return self.CityId


class State(models.Model):

    StateId=IntegerField(primary_key=True)#models.ForeignKey(to=City)
    CountryId=IntegerField()
    Name=CharField(max_length=200)
    Description=CharField(max_length=500)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="State"

    def __str__(self):
        return self.StateId


class Country(models.Model):

    #primary_key=True CountryId

    CountryId=IntegerField(primary_key=True)#models.ForeignKey(to=State)#
    CountryName=CharField(max_length=200)
    Description=CharField(max_length=500)
    ActiveFlag=BooleanField(default=0)

    class Meta:
        db_table="Country"

    def __str__(self):
        return self.CountryId
