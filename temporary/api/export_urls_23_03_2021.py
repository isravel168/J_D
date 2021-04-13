#ENDPOINTS and payloads for JobCategory

# https://homeurl/api/jobcategory/
# https://homeurl/api/detailed/jobcategory/(key for process(JobCategoryCode))
# https://homeurl/api/create/jobcategory/
# https://homeurl/api/update/jobcategory/(key for process(JobCategoryCode))
# https://homeurl/api/delete/jobcategory/(key for process(JobCategoryCode))

"""
 {
        "JobCategoryCode": "JC00000006",
        "JobCatDescription": "Customer Service",
        "JobCatCreatedBy": "Patnaik",
        "JobCatCreatedDate": "2021-03-22",
        "JobCatUpdatedBy": "Subramanian",
        "JobCatUpdatedDate": "2021-03-22",
        "JobCatDelFlag": true
    }
"""

#ENDPOINTS and payloads for JobTitle

# https://homeurl/api/jobtitle/
# https://homeurl/api/detailed/jobtitle/(key for process(JobTttleCode))
# https://homeurl/api/create/jobtitle/
# https://homeurl/api/update/jobtitle/(key for process(JobTttleCode))
# https://homeurl/api/delete/jobtitle/(key for process(JobTttleCode))
"""
    {
        "JobTtlCategoryCode": "JC00000001",
        "JobTttleCode": "JT00000026",
        "JobTitleDescription": "Mortgage Loan Processor job description",
        "JobTitleCreatedBy": "Patnaik",
        "JobTitleCreatedDate": "2021-02-01",
        "JobTitleUpdatedBy": "Subramanian",
        "JobTitleUpdatedDate": "2021-02-05",
        "JobTitleDelFlag": true
    }
"""


#ENDPOINTS and payloads for JobBrief

# https://homeurl/api/jobbrief/
# https://homeurl/api/detailed/jobbrief/(key for process(JobBrfCode))
# https://homeurl/api/create/jobbrief/
# https://homeurl/api/update/jobbrief/(key for process(JobBrfCode))
# https://homeurl/api/delete/jobbrief/(key for process(JobBrfCode))
"""
   {
        "JobBrfCatCode": "JC00000001",
        "JobBrfTtlCode": "JT00000001",
        "JobBrfCode": "JBF0000001",
        "JobBrfDescription": "We are looking for a cost analyst to help us audit our expenses and find ways to make our operations more cost-efficient.",
        "JobBrfCreatedBy": "Patnaik",
        "JobBrfCreatedDate": "2021-02-01",
        "JobBrfUpdatedBy": "Subramanian",
        "JobBrfUpdatedDate": "2021-02-05",
        "JobBrfDelFlag": false
    }
"""


#ENDPOINTS and payloads for jobresponsibility

# https://homeurl/api/jobresponsibility/
# https://homeurl/api/detailed/jobresponsibility/(key for process(JobResposibleCode))
# https://homeurl/api/create/jobresponsibility/
# https://homeurl/api/update/jobresponsibility/(key for process(JobResposibleCode))
# https://homeurl/api/delete/jobresponsibility/(key for process(JobResposibleCode))
"""
    {
        "JobResCatCode": "JC00000001",
        "JobResTtlCode": "JT00000002",
        "JobResposibleCode": "JRS0000022",
        "JobResponsibleDescription": "Ensure compliance with governmental laws on payroll accounting and taxes",
        "JobResCreatedBy": "Patnaik",
        "JobResCreatedDate": "2021-03-22",
        "JobResUpdatedBy": "Subramanian",
        "JobResUpdatedDate": "2021-03-22",
        "JobResDelFlag": true
    }

"""


#ENDPOINTS and payloads for jobrequirement

# https://homeurl/api/jobrequirement/
# https://homeurl/api/detailed/jobrequirement/(key for process(JobReqCode))
# https://homeurl/api/create/jobrequirement/
# https://homeurl/api/update/jobrequirement/(key for process(JobReqCode))
# https://homeurl/api/delete/jobrequirement/(key for process(JobReqCode))
"""
    {
        "JobReqCatCode": "JC00000001",
        "JobReqTtlCode": "JT00000003",
        "JobReqCode": "JRQ0000019",
        "JobReqDescription": "Comprehensive understanding of government tax laws",
        "JobReqCreatedBy": "Patnaik",
        "JobReqCreatedDate": "2021-02-01",
        "JobReqUpdatedBy": "Subramanian",
        "JobReqUpdatedDate": "2021-02-05",
        "JobReqDelFlag": false
    }
"""


#ENDPOINTS and payloads for jobinterviewquestion

# https://homeurl/api/jobinterviewquestion/
# https://homeurl/api/detailed/jobinterviewquestion/(key for process(JobIntQuesCode))
# https://homeurl/api/create/jobinterviewquestion/
# https://homeurl/api/update/jobinterviewquestion/(key for process(JobIntQuesCode))
# https://homeurl/api/delete/jobinterviewquestion/(key for process(JobIntQuesCode))

"""
    {
        "JobIntQuesCode": "JT00000001",
        "JobIntQuesCatCode": "JC00000001",
        "JobIntQuesTtlCode": "JT00000001",
        "JobIntQuesType": "Operation & Situational Questions",
        "JobIntQuesDescription": "If you could use only Excel, how would you organize the company’s fixed costs to ensure they’re accurate and accessible?",
        "JobIntQuesCreatedBy": "Patnaik",
        "JobIntQuesCreatedDate": "2021-02-01",
        "JobIntQuesUpdatedBy": "Subramanian",
        "JobIntQuesUpdatedDate": "2021-02-05",
        "JJobIntQuesDelFlag": false
    }
"""
