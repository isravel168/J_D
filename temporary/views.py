import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .api.serializers import JobCategorySerializer
from .functions import storeJobCategory
# Create your views here.
from .models import JobCategory


def temporary(request):

    from django.http import HttpResponse
    while True:
        try:
            #storeJobCategory(**{"file_name":"resources/Job Description database.xls","sheet_name":"Job Category"})
            #storeJobCategory(**{"file_name": "resources/Job Description database.xls", "sheet_name": "Job Title"})
            #storeJobCategory(**{"file_name": "resources/Job Description database.xls", "sheet_name": "Job Responsibity"})
            #storeJobCategory(**{"file_name": "resources/Job Description database.xls", "sheet_name": "Job Requirement"})
            #storeJobCategory(**{"file_name": "resources/Job Description database.xls", "sheet_name": "Job Brief"})
            #storeJobCategory(**{"file_name": "resources/Job Description database.xls", "sheet_name": "Job Interview Questions"})
            return HttpResponse("Data got stored stored successfully!")
        except Exception as e:
            return HttpResponse("Error prevailed",str(e))
    return render(request,"index.html")

