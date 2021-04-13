import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from ..models import JobCategory, JobTitle, JobBrief, JobResponsibility, JobRequirement, JobInterviewQuestion, \
    City, Qualification, Skill, Perks, State, Country, Invoice, Payment, Plan, SalesLead, CustomerMaster, \
     Subscriptions,  \
     CancellationPlan, Enquiry
from .serializers import JobCategorySerializer, JobTitleSerializer, JobBriefSerializer, \
    JobResponsibilitySerializer, JobRequirementSerializer, \
    QualificationSerializer, SkillSerializer, PerksSerializer, \
    InvoiceSerializer, PaymentSerializer, PlanSerializer, SalesLeadSerializer, CustomerMasterSerializer, \
    SubscriptionsSerializer, JobInterviewQuestionSerializer, \
 \
    CancellationPlanSerializer, EnquirySerializer, CitySerializer, StateSerializer, CountrySerializer


@api_view(['GET', 'POST', 'DELETE','PUT'])
def enquiry(request,pk=None):
    if pk is not None:
        try:
            tutorial = Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = EnquirySerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Enquiry.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = EnquirySerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Enquiry.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Enquiry.objects.get(pk=pk)
                    serializer = EnquirySerializer(book)
                    return JsonResponse({'Enquiry': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = EnquirySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Enquiry.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The Enquiry '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Enquiry.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Enquiry.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} Enquirys were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def customerMaster(request,pk=None):
    if pk is not None:
        try:
            tutorial = CustomerMaster.objects.get(pk=pk)
        except CustomerMaster.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = CustomerMasterSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = CustomerMaster.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CustomerMasterSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = CustomerMaster.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = CustomerMaster.objects.get(pk=pk)
                    serializer = CustomerMasterSerializer(book)
                    return JsonResponse({'customerMaster': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = CustomerMasterSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = CustomerMaster.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The customerMaster '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except CustomerMaster.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = CustomerMaster.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} customerMaster were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def plan(request,pk=None):
    if pk is not None:
        try:
            tutorial = Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = PlanSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Plan.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = PlanSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Plan.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Plan.objects.get(pk=pk)
                    serializer = PlanSerializer(book)
                    return JsonResponse({'plan': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = PlanSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Plan.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The plan '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Plan.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Plan.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} plans were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def subscriptions(request,pk=None):
    if pk is not None:
        try:
            tutorial = Subscriptions.objects.get(pk=pk)
        except Subscriptions.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = SubscriptionsSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Subscriptions.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = SubscriptionsSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Subscriptions.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Subscriptions.objects.get(pk=pk)
                    serializer = SubscriptionsSerializer(book)
                    return JsonResponse({'Subscriptions': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = SubscriptionsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Subscriptions.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The Subscription '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Subscriptions.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Subscriptions.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} Subscriptions were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def salesLead(request,pk=None):
    if pk is not None:
        try:
            tutorial = SalesLead.objects.get(pk=pk)
        except SalesLead.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = SalesLeadSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = SalesLead.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = SalesLeadSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = SalesLead.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = SalesLead.objects.get(pk=pk)
                    serializer = SalesLeadSerializer(book)
                    return JsonResponse({'salesLead': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = SalesLeadSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = SalesLead.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The salesLead  '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except SalesLead.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = SalesLead.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} salesLeads were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def invoice(request,pk=None):
    if pk is not None:
        try:
            tutorial = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = InvoiceSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Invoice.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = InvoiceSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Invoice.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Invoice.objects.get(pk=pk)
                    serializer = InvoiceSerializer(book)
                    return JsonResponse({'invoice': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = InvoiceSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Invoice.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The invoice '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Invoice.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Invoice.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} invoice were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def payment(request,pk=None):
    if pk is not None:
        try:
            tutorial = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = PaymentSerializer(tutorial)
            if len(tutorial_serializer.data)==0:
                return JsonResponse("Requested Data is not exist.")
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Payment.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = PaymentSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Payment.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Payment.objects.get(pk=pk)
                    serializer = PaymentSerializer(book)
                    return JsonResponse({'payment': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = PaymentSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Payment.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The payment '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Payment.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Payment.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} payments were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def qualification(request,pk=None):
    if pk is not None:
        try:
            tutorial = Qualification.objects.get(pk=pk)
        except Qualification.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = QualificationSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Qualification.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = QualificationSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Qualification.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Qualification.objects.get(pk=pk)
                    serializer = QualificationSerializer(book)
                    return JsonResponse({'qualification': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = QualificationSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Qualification.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The qualification '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Qualification.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Qualification.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} qualification were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})

@api_view(['GET', 'POST', 'DELETE','PUT'])
def skill(request,pk=None):
    if pk is not None:
        try:
            tutorial = Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = SkillSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Skill.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = SkillSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Skill.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Skill.objects.get(pk=pk)
                    serializer = SkillSerializer(book)
                    return JsonResponse({'skill': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = SkillSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Skill.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The skill '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Skill.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Skill.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} skill were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})



@api_view(['GET', 'POST', 'DELETE','PUT'])
def perks(request,pk=None):
    if pk is not None:
        try:
            tutorial = Perks.objects.get(pk=pk)
        except Perks.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = PerksSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Perks.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = PerksSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Perks.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Perks.objects.get(pk=pk)
                    serializer = PerksSerializer(book)
                    return JsonResponse({'perks': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = PerksSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Perks.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The perk '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Perks.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Perks.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} perks were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def cancellationPlan(request, pk=None):
    if pk is not None:
        try:
            tutorial = CancellationPlan.objects.get(pk=pk)
        except CancellationPlan.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = CancellationPlanSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = CancellationPlan.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CancellationPlanSerializer(tutorials, many=True)
        if len(tutorials_serializer.data) == 0:
            return JsonResponse({"message": "Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = CancellationPlan.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = CancellationPlan.objects.get(pk=pk)
                    serializer = CancellationPlanSerializer(book)
                    return JsonResponse({'CancellationPlan': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = CancellationPlanSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = CancellationPlan.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The CancellationPlan ' + str(pk) + ' got deleted'},
                                    status=status.HTTP_204_NO_CONTENT)
            except CancellationPlan.DoesNotExist:
                return JsonResponse({'message': 'Requested Data ' + str(pk) + ' is not exist.'},
                                    status=status.HTTP_404_NOT_FOUND)

        count = CancellationPlan.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} CancellationPlans were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message": "No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def jobResponsibility(request, pk=None):
    if pk is not None:
        try:
            tutorial = JobResponsibility.objects.get(pk=pk)
        except JobResponsibility.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobResponsibilitySerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobResponsibility.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobResponsibilitySerializer(tutorials, many=True)
        if len(tutorials_serializer.data) == 0:
            return JsonResponse({"message": "Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobResponsibility.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobResponsibility.objects.get(pk=pk)
                    serializer = JobResponsibilitySerializer(book)
                    return JsonResponse({'jobResponsibility': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobResponsibilitySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobResponsibility.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobResponsibility ' + str(pk) + ' got deleted'},
                                    status=status.HTTP_204_NO_CONTENT)
            except JobResponsibility.DoesNotExist:
                return JsonResponse({'message': 'Requested Data ' + str(pk) + ' is not exist.'},
                                    status=status.HTTP_404_NOT_FOUND)

        count = JobResponsibility.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobResponsibility were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message": "No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def jobRequirement(request, pk=None):
    if pk is not None:
        try:
            tutorial = JobRequirement.objects.get(pk=pk)
        except JobRequirement.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobRequirementSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobRequirement.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobRequirementSerializer(tutorials, many=True)
        if len(tutorials_serializer.data) == 0:
            return JsonResponse({"message": "Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobRequirement.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobRequirement.objects.get(pk=pk)
                    serializer = JobRequirementSerializer(book)
                    return JsonResponse({'jobRequirement': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobRequirementSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobRequirement.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobRequirement ' + str(pk) + ' got deleted'},
                                    status=status.HTTP_204_NO_CONTENT)
            except JobRequirement.DoesNotExist:
                return JsonResponse({'message': 'Requested Data ' + str(pk) + ' is not exist.'},
                                    status=status.HTTP_404_NOT_FOUND)

        count = JobRequirement.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobRequirements were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message": "No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def jobBrief(request,pk=None):
    if pk is not None:
        try:
            tutorial = JobBrief.objects.get(pk=pk)
        except JobBrief.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobBriefSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobBrief.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobBriefSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobBrief.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobBrief.objects.get(pk=pk)
                    serializer = JobBriefSerializer(book)
                    return JsonResponse({'jobBrief': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobBriefSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobBrief.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobBrief  '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except JobBrief.DoesNotExist:
                print("999")
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = JobBrief.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobBrief were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})



@api_view(['GET', 'POST', 'DELETE','PUT'])
def jobCategory(request,pk=None):
    if pk is not None:
        try:
            tutorial = JobCategory.objects.get(pk=pk)
        except JobCategory.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobCategorySerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobCategory.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobCategorySerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobCategory.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobCategory.objects.get(pk=pk)
                    serializer = JobCategorySerializer(book)
                    return JsonResponse({'jobCategory': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobCategorySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobCategory.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobCategory '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except JobCategory.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = JobCategory.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobCategory were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})

@api_view(['GET', 'POST', 'DELETE','PUT'])
def jobTitle(request,pk=None):
    if pk is not None:
        try:
            tutorial = JobTitle.objects.get(pk=pk)
        except JobTitle.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobTitleSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobTitle.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobTitleSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobTitle.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobTitle.objects.get(pk=pk)
                    serializer = JobTitleSerializer(book)
                    return JsonResponse({'jobTitle': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobTitleSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobTitle.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobTitle '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except JobTitle.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = JobTitle.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobTitle were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})



@api_view(['GET', 'POST', 'DELETE','PUT'])
def jobInterviewQuestion(request,pk=None):
    if pk is not None:
        try:
            tutorial = JobInterviewQuestion.objects.get(pk=pk)
        except JobInterviewQuestion.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobInterviewQuestionSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobInterviewQuestion.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobInterviewQuestionSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobInterviewQuestion.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobInterviewQuestion.objects.get(pk=pk)
                    serializer = JobInterviewQuestionSerializer(book)
                    return JsonResponse({'jobInterviewQuestion': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobInterviewQuestionSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobInterviewQuestion.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The jobInterviewQuestion '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except JobInterviewQuestion.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = JobInterviewQuestion.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} jobInterviewQuestions were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})




@api_view(['GET', 'POST', 'DELETE','PUT'])
def city(request,pk=None):
    if pk is not None:
        try:
            tutorial = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = CitySerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = City.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CitySerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = City.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = City.objects.get(pk=pk)
                    serializer = CitySerializer(book)
                    return JsonResponse({'City': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = CitySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = City.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The Subscription '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except City.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = City.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} City were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})

@api_view(['GET', 'POST', 'DELETE','PUT'])
def state(request,pk=None):
    if pk is not None:
        try:
            tutorial = State.objects.get(pk=pk)
        except State.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = StateSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = State.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = StateSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = State.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = State.objects.get(pk=pk)
                    serializer = StateSerializer(book)
                    return JsonResponse({'State': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = StateSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = State.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The Subscription '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except State.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = State.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} State were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})

@api_view(['GET', 'POST', 'DELETE','PUT'])
def country(request,pk=None):
    if pk is not None:
        try:
            tutorial = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = CountrySerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = Country.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CountrySerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = Country.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = Country.objects.get(pk=pk)
                    serializer = CountrySerializer(book)
                    return JsonResponse({'Country': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = CountrySerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = Country.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The Subscription '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except Country.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = Country.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} Country were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})
