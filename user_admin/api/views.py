import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from user_admin.api.serializers import AddLicenseSerializer, ReduceLicenseSerializer
from .serializers import RequestForCancelPlanSerializer
from ..models import AddLicense, ReduceLicense, RequestForCancelPlan

"""
decorator (function) which allows to function the below function only
when the request is GET, POST, DELETE and PUT.
"""
@api_view(['GET', 'POST', 'DELETE','PUT'])
def addLicense(request,pk=None):
    """
    Function will perform CRUD based on the receiving primary key.  Operations will get done on AddLicense Entity.
    :param request: Browser Request Object.
    :param pk: primary key for AddLicense entity.
    :return: JsonResponse.
    """
    if pk is not None:
        """
        if pk is not None, We try to get the instance for the given pk. else we raise Exception.  Operation will
        get a specific instance Details.
        """
        try:
            tutorial = AddLicense.objects.get(pk=pk)
        except AddLicense.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = AddLicenseSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    """
    if pk is None, We try to get all instances. else we raise Exception.  Operation will
    get a brought of many instances from AddLicense Entity.
    """
    if request.method == 'GET':
        tutorials = AddLicense.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = AddLicenseSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            """
            if length of the fetched data is Zero,  We send info which "no data fetched" to user Browser.
            """
            return JsonResponse({"message":"Requested Data is not exist."})
        """
        if length of the fetched data is not Zero,  We send the fetched data  to user Browser.
        """
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = AddLicense.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = AddLicense.objects.get(pk=pk)
                    serializer = AddLicenseSerializer(book)
                    return JsonResponse({'AddLicense': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = AddLicenseSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = AddLicense.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The AddLicense '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except AddLicense.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = AddLicense.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} AddLicenses were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def reduceLicense(request,pk=None):
    if pk is not None:
        try:
            tutorial = ReduceLicense.objects.get(pk=pk)
        except ReduceLicense.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = ReduceLicenseSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = ReduceLicense.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = ReduceLicenseSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = ReduceLicense.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = ReduceLicense.objects.get(pk=pk)
                    serializer = ReduceLicenseSerializer(book)
                    return JsonResponse({'ReduceLicense': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ReduceLicenseSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = ReduceLicense.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The ReduceLicense '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except ReduceLicense.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = ReduceLicense.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} ReduceLicenses were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


@api_view(['GET', 'POST', 'DELETE','PUT'])
def requestForCancelPlan(request,pk=None):
    if pk is not None:
        try:
            tutorial = RequestForCancelPlan.objects.get(pk=pk)
        except RequestForCancelPlan.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = RequestForCancelPlanSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = RequestForCancelPlan.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = RequestForCancelPlanSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = RequestForCancelPlan.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = RequestForCancelPlan.objects.get(pk=pk)
                    serializer = RequestForCancelPlanSerializer(book)
                    return JsonResponse({'RequestForCancelPlan': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = RequestForCancelPlanSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = RequestForCancelPlan.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The RequestForCancelPlan '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except RequestForCancelPlan.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = RequestForCancelPlan.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} RequestForCancelPlans were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})





