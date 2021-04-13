from .models import JobCategory, JobTitle,JobResponsibility,JobRequirement,JobBrief,JobInterviewQuestion
def storeJobCategory(**kwargs):
    import pandas
    try:
        file_name=kwargs.get('file_name')
        sheet_name=kwargs.get('sheet_name')
        excel_data_df = pandas.read_excel(file_name, sheet_name=sheet_name)

        if sheet_name=="Job Category":
            for item in excel_data_df.to_numpy():
                print(item)
                j_category=JobCategory(JobCategoryId=item[0],\
                                       Name=item[1],\
                                       Description=item[1],\

                                       ApprovalFlag=item[6],\
                                       ClientSpecificFlag=item[6],\
                                       CreatedBy=item[4],CreatedDate="",ModifiedBy="",ModifiedDate="",ActiveFlag=True)
                j_category.save()
            return 1

        if sheet_name=="Job Title":
            for item in excel_data_df.to_numpy():
                j_title=JobTitle(JobTtlCategoryCode=item[0],\
                                       JobTttleCode=item[1],\
                                       JobTitleDescription=item[2],\
                                       JobTitleCreatedBy=item[3],\
                                       JobTitleCreatedDate=item[4],\
                                       JobTitleUpdatedBy=item[5],\
                                       JobTitleUpdatedDate=item[6],\
                                        JobTitleDelFlag=item[7])
                j_title.save()
            return 1

        if sheet_name=="Job Responsibity":
            for item in excel_data_df.to_numpy():
                j_responsibility=JobResponsibility(
                    JobResCatCode=item[0],\
                    JobResTtlCode=item[1],\
                    JobResposibleCode = item[2],\
                    JobResponsibleDescription = item[3],\
                    JobResCreatedBy = item[4],\
                    JobResCreatedDate = item[5],\
                    JobResUpdatedBy = item[6],\
                    JobResUpdatedDate = item[7],\
                    JobResDelFlag = item[8])
                j_responsibility.save()
            return 1

        if sheet_name == "Job Requirement":
            for item in excel_data_df.to_numpy():
                j_requirement = JobRequirement(
                    JobReqCatCode=item[0], \
                    JobReqTtlCode=item[1], \
                    JobReqCode=item[2], \
                    JobReqDescription=item[3], \
                    JobReqCreatedBy=item[4], \
                    JobReqCreatedDate=item[5], \
                    JobReqUpdatedBy=item[6], \
                    JobReqUpdatedDate=item[7], \
                    JobReqDelFlag=item[8])
                j_requirement.save()
            return 1

        if sheet_name == "Job Brief":
            for item in excel_data_df.to_numpy():
                j_brief = JobBrief(
                    JobBrfCatCode=item[0], \
                    JobBrfTtlCode=item[1], \
                    JobBrfCode=item[2], \
                    JobBrfDescription=item[3], \
                    JobBrfCreatedBy=item[4], \
                    JobBrfCreatedDate=item[5], \
                    JobBrfUpdatedBy=item[6], \
                    JobBrfUpdatedDate=item[7], \
                    JobBrfDelFlag=item[8])
                j_brief.save()
            return 1

        if sheet_name == "Job Interview Questions":

            for item in excel_data_df.to_numpy():
                j_interviewquestion = JobInterviewQuestion(
                    JobIntQuesCatCode=int(item[0]), \
                    JobIntQuesTtlCode=int(item[1]), \
                    JobIntQuesType=item[3], \
                    JobIntQuesCode=item[2], \
                    JobIntQuesDescription=item[4], \
                    JobIntQuesCreatedBy=item[5], \
                    JobIntQuesCreatedDate=item[6], \
                    JobIntQuesUpdatedBy=item[7], \
                    JobIntQuesUpdatedDate=item[8],\
                    JJobIntQuesDelFlag=item[9])
                j_interviewquestion.save()
            return 1

    except Exception as e:
        print(str(e))
        raise str(e)


