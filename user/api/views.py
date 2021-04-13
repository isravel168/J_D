import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import MyJobDescriptionSerializer, JobPostingSerializer, UserMasterSerializer
from ..models import MyJobDescription, UserMaster, JobPosting


@api_view(['GET', 'POST', 'DELETE','PUT'])
def userProfile(request,pk=None):
    if pk is not None:
        try:
            tutorial = UserMaster.objects.get(pk=pk)
        except UserMaster.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = UserMasterSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = UserMaster.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = UserMasterSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = UserMaster.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = UserMaster.objects.get(pk=pk)
                    serializer = UserMasterSerializer(book)
                    return JsonResponse({'UserMaster': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = UserMasterSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = UserMaster.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The UserMaster '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except UserMaster.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = UserMaster.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} UserMasters were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})



@api_view(['GET', 'POST', 'DELETE','PUT'])
def myJobDescription(request,pk=None):
    if pk is not None:
        try:
            tutorial = MyJobDescription.objects.get(pk=pk)
        except MyJobDescription.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = MyJobDescriptionSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = MyJobDescription.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = MyJobDescriptionSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = MyJobDescription.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = MyJobDescription.objects.get(pk=pk)
                    serializer = MyJobDescriptionSerializer(book)
                    return JsonResponse({'MyJobDescription': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = MyJobDescriptionSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = MyJobDescription.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The MyJobDescription '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except MyJobDescription.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = MyJobDescription.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} MyJobDescriptions were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})



@api_view(['GET', 'POST', 'DELETE','PUT'])
def jobPosting(request,pk=None):
    if pk is not None:
        try:
            tutorial = JobPosting.objects.get(pk=pk)
        except JobPosting.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = JobPostingSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = JobPosting.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = JobPostingSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = JobPosting.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = JobPosting.objects.get(pk=pk)
                    serializer = JobPostingSerializer(book)
                    return JsonResponse({'JobPosting': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = JobPostingSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = JobPosting.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The JobPosting '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except JobPosting.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = JobPosting.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} JobPostings were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})


