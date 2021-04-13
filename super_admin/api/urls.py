from django.conf.urls import url
from . import views
from .views import  jobCategory, \
    jobTitle, SalesLead, salesLead, customerMaster, jobBrief, jobResponsibility, jobRequirement, jobInterviewQuestion, \
    city, state, country, qualification, skill, perks, invoice, payment, plan, \
    subscriptions, cancellationPlan, \
    enquiry

urlpatterns = [


        url(r'^enquiry/$', enquiry),  # SalesLeadListView.as_view()),
        url(r'^enquiry/(?P<pk>[-\w]+)', enquiry),  # SalesLeadDetailView.as_view()),
        url(r'^enquiry/$', enquiry),  # SalesLeadCreateApi.as_view()),
        url(r'^enquiry/(?P<pk>[-\w]+)', enquiry),  # SalesLeadUpdateApi.as_view()),
        url(r'^enquiry/(?P<pk>[-\w]+)', enquiry),  # SalesLeadDeleteApi.as_view())

        url(r'^customermaster/$', customerMaster),  # SalesLeadListView.as_view()),
        url(r'^customermaster/(?P<pk>[-\w]+)', customerMaster),  # SalesLeadDetailView.as_view()),
        url(r'^customermaster/$', customerMaster),  # SalesLeadCreateApi.as_view()),
        url(r'^customermaster/(?P<pk>[-\w]+)', customerMaster),  # SalesLeadUpdateApi.as_view()),
        url(r'^customermaster/(?P<pk>[-\w]+)', customerMaster),  # SalesLeadDeleteApi.as_view())

        url(r'^plan/$', plan),  # PlanListView.as_view()),
        url(r'^plan/(?P<pk>[-\w]+)', plan),  # PlanDetailView.as_view()),
        url(r'^plan/$', plan),  # PlanCreateApi.as_view()),
        url(r'^plan/(?P<pk>[-\w]+)', plan),  # PlanUpdateApi.as_view()),
        url(r'^plan/(?P<pk>[-\w]+)', plan),  # PlanDeleteApi.as_view()),

        url(r'^subscriptions/$', subscriptions),  # SalesLeadListView.as_view()),
        url(r'^subscriptions/(?P<pk>[-\w]+)', subscriptions),  # SalesLeadDetailView.as_view()),
        url(r'^subscriptions/$', subscriptions),  # SalesLeadCreateApi.as_view()),
        url(r'^subscriptions/(?P<pk>[-\w]+)', subscriptions),  # SalesLeadUpdateApi.as_view()),
        url(r'^subscriptions/(?P<pk>[-\w]+)', subscriptions),  # SalesLeadDeleteApi.as_view())

        url(r'^saleslead/$', salesLead),  # SalesLeadListView.as_view()),
        url(r'^saleslead/(?P<pk>[-\w]+)', salesLead),  # SalesLeadDetailView.as_view()),
        url(r'^saleslead/$', salesLead),  # SalesLeadCreateApi.as_view()),
        url(r'^saleslead/(?P<pk>[-\w]+)', salesLead),  # SalesLeadUpdateApi.as_view()),
        url(r'^saleslead/(?P<pk>[-\w]+)', salesLead),  # SalesLeadDeleteApi.as_view())

        url(r'^invoice/$', invoice),  # InvoiceListView.as_view()),
        url(r'^invoice/(?P<pk>[-\w]+)', invoice),  # InvoiceDetailView.as_view()),
        url(r'^invoice/$', invoice),  # InvoiceCreateApi.as_view()),
        url(r'^invoice/(?P<pk>[-\w]+)', invoice),  # InvoiceUpdateApi.as_view()),
        url(r'^invoice/(?P<pk>[-\w]+)', invoice),  # InvoiceDeleteApi.as_view()),

        url(r'^payment/$', payment),  # PaymentListView.as_view()),
        url(r'^payment/(?P<pk>[-\w]+)', payment),  # PaymentDetailView.as_view()),
        url(r'^payment/$', payment),  # PaymentCreateApi.as_view()),
        url(r'^payment/(?P<pk>[-\w]+)', payment),  # PaymentUpdateApi.as_view()),
        url(r'^payment/(?P<pk>[-\w]+)', payment),  # PaymentDeleteApi.as_view()),

        # qualification
        url(r'^qualification/$', qualification),  # QualificationListView.as_view()),
        url(r'^qualification/(?P<pk>[-\w]+)', qualification),  # QualificationDetailView.as_view()),
        url(r'^qualification/$', qualification),  # QualificationCreateApi.as_view()),
        url(r'^qualification/(?P<pk>[-\w]+)', qualification),  # QualificationUpdateApi.as_view()),
        url(r'^qualification/(?P<pk>[-\w]+)', qualification),  # QualificationDeleteApi.as_view()),

        # skill
        url(r'^skill/$', skill),  # SkillListView.as_view()),
        url(r'^skill/(?P<pk>[-\w]+)', skill),  # SkillDetailView.as_view()),
        url(r'^skill/$', skill),  # SkillCreateApi.as_view()),
        url(r'^skill/(?P<pk>[-\w]+)', skill),  # SkillUpdateApi.as_view()),
        url(r'^skill/(?P<pk>[-\w]+)', skill),  # SkillDeleteApi.as_view()),

        # perks
        url(r'^perks/$', perks),  # PerksListView.as_view()),
        url(r'^perks/(?P<pk>[-\w]+)', perks),  # PerksDetailView.as_view()),
        url(r'^perks/$', perks),  # PerksCreateApi.as_view()),
        url(r'^perks/(?P<pk>[-\w]+)', perks),  # PerksUpdateApi.as_view()),
        url(r'^perks/(?P<pk>[-\w]+)', perks),  # PerksDeleteApi.as_view()),

        url(r'^cancellationplan/$', cancellationPlan),  # SalesLeadListView.as_view()),
        url(r'^cancellationplan/(?P<pk>[-\w]+)', cancellationPlan),  # SalesLeadDetailView.as_view()),
        url(r'^cancellationplan/$', cancellationPlan),  # SalesLeadCreateApi.as_view()),
        url(r'^cancellationplan/(?P<pk>[-\w]+)', cancellationPlan),  # SalesLeadUpdateApi.as_view()),
        url(r'^cancellationplan/(?P<pk>[-\w]+)', cancellationPlan),  # SalesLeadDeleteApi.as_view())

        # Job Responsiblity
        url(r'^jobresponsibility/$', jobResponsibility),  # JobResponsibilityListView.as_view()),
        url(r'^jobresponsibility/(?P<pk>[-\w]+)', jobResponsibility),  # JobResponsibilityDetailView.as_view()),
        url(r'^jobresponsibility/$', jobResponsibility),  # JobResponsibilityCreateApi.as_view()),
        url(r'^jobresponsibility/(?P<pk>[-\w]+)', jobResponsibility),  # JobResponsibilityUpdateApi.as_view()),
        url(r'^jobresponsibility/(?P<pk>[-\w]+)', jobResponsibility),  # JobResponsibilityDeleteApi.as_view()),

        # Job Requirement
        url(r'^jobrequirement/$', jobRequirement),  # JobRequirementListView.as_view()),
        url(r'^jobrequirement/(?P<pk>[-\w]+)', jobRequirement),  # JobRequirementDetailView.as_view()),
        url(r'^jobrequirement/$', jobRequirement),  # JobRequirementCreateApi.as_view()),
        url(r'^jobrequirement/(?P<pk>[-\w]+)', jobRequirement),  # JobRequirementUpdateApi.as_view()),
        url(r'^jobrequirement/(?P<pk>[-\w]+)', jobRequirement),  # JobRequirementDeleteApi.as_view()),

        # Job Brief
        url(r'^jobbrief/$', jobBrief),  # JobBriefListView.as_view()),
        url(r'^jobbrief/(?P<pk>[-\w]+)', jobBrief),  # JobBriefDetailView.as_view()),
        url(r'^jobbrief/$', jobBrief),  # JobBriefCreateApi.as_view()),
        url(r'^jobbrief/(?P<pk>[-\w]+)', jobBrief),  # jobBrief),# JobBriefUpdateApi.as_view()),
        url(r'^jobbrief/(?P<pk>[-\w]+)', jobBrief),  # JobBriefDeleteApi.as_view()),

        # Job Category
        url(r'^jobcategory/$', jobCategory),  # JobCategoryListView.as_view()),
        url(r'^jobcategory/(?P<pk>[-\w]+)', jobCategory),  # JobCategoryDetailView.as_view()),
        url(r'^jobcategory/$', jobCategory),  # JobCategoryCreateApi.as_view()),
        url(r'^jobcategory/(?P<pk>[-\w]+)', jobCategory),  # ,views.JobCategoryUpdateApi.as_view()),
        url(r'^jobcategory/(?P<pk>[-\w]+)', jobCategory),  # ,views.JobCategoryDeleteApi.as_view()),

        # Job Title
        url(r'^jobtitle/$', jobTitle),  # JobTitleListView.as_view()),
        url(r'^jobtitle/(?P<pk>[-\w]+)', jobTitle),  # JobTitleDetailView.as_view()),
        url(r'^jobtitle/$', jobTitle),  # JobTitleCreateApi.as_view()),
        url(r'^jobtitle/(?P<pk>[-\w]+)', jobTitle),  # JobTitleUpdateApi.as_view()),
        url(r'^jobtitle/(?P<pk>[-\w]+)', jobTitle),  # JobTitleDeleteApi.as_view()),

        # Job InterviewQuestion
        url(r'^jobinterviewquestion/$', jobInterviewQuestion),  # JobInterviewQuestionListView.as_view()),
        url(r'^jobinterviewquestion/(?P<pk>[-\w]+)', jobInterviewQuestion),  # JobInterviewQuestionDetailView.as_view()),
        url(r'^jobinterviewquestion/$', jobInterviewQuestion),  # JobInterviewQuestionCreateApi.as_view()),
        url(r'^jobinterviewquestion/(?P<pk>[-\w]+)', jobInterviewQuestion),  # JobInterviewQuestionUpdateApi.as_view()),
        url(r'^jobinterviewquestion/(?P<pk>[-\w]+)', jobInterviewQuestion),  # JobInterviewQuestionDeleteApi.as_view()),

        # City
        url(r'^city/$', city),  # CityListView.as_view()),
        url(r'^city/(?P<pk>[-\w]+)', city),  # CityDetailView.as_view()),
        url(r'^city/$', city),  # CityCreateApi.as_view()),
        url(r'^city/(?P<pk>[-\w]+)', city),  # CityUpdateApi.as_view()),
        url(r'^city/(?P<pk>[-\w]+)', city),  # CityDeleteApi.as_view()),

        # State
        url(r'^state/$', state),  # StateListView.as_view()),
        url(r'^state/(?P<pk>[-\w]+)', state),  # StateDetailView.as_view()),
        url(r'^state/$', state),  # StateCreateApi.as_view()),
        url(r'^state/(?P<pk>[-\w]+)', state),  # StateUpdateApi.as_view()),
        url(r'^state/(?P<pk>[-\w]+)', state),  # StateDeleteApi.as_view()),

        # country
        url(r'^country/$', country),  # CountryListView.as_view()),
        url(r'^country/(?P<pk>[-\w]+)', country),  # CountryDetailView.as_view()),
        url(r'^country/$', country),  # CountryCreateApi.as_view()),
        url(r'^country/(?P<pk>[-\w]+)', country),  # CountryUpdateApi.as_view()),
        url(r'^country/(?P<pk>[-\w]+)', country),  # CountryDeleteApi.as_view()),

]