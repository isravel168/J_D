import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from ..models import AddOrCancelRequest
from .serializers import  AddOrCancelRequestSerializer

@api_view(['GET', 'POST', 'DELETE','PUT'])
def addOrCancelRequest(request,pk=None):
    if pk is not None:
        try:
            tutorial = AddOrCancelRequest.objects.get(pk=pk)
        except AddOrCancelRequest.DoesNotExist:
            return JsonResponse({'message': 'Requested Data is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            tutorial_serializer = AddOrCancelRequestSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)

    if request.method == 'GET':
        tutorials = AddOrCancelRequest.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = AddOrCancelRequestSerializer(tutorials, many=True)
        if len(tutorials_serializer.data)==0:
            return JsonResponse({"message":"Requested Data is not exist."})
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == "PUT":
        if pk is not None:
            try:
                payload = json.loads(request.body)
                try:
                    book_item = AddOrCancelRequest.objects.filter(pk=pk)
                    # returns 1 or 0
                    book_item.update(**payload)
                    book = AddOrCancelRequest.objects.get(pk=pk)
                    serializer = AddOrCancelRequestSerializer(book)
                    return JsonResponse({'AddOrCancelRequest': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except ObjectDoesNotExist as e:
                    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = AddOrCancelRequestSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                tutorial = AddOrCancelRequest.objects.get(pk=pk)
                tutorial.delete()
                return JsonResponse({'message': 'The AddOrCancelRequest '+str(pk)+' got deleted'}, status=status.HTTP_204_NO_CONTENT)
            except AddOrCancelRequest.DoesNotExist:
                return JsonResponse({'message': 'Requested Data '+str(pk)+' is not exist.'}, status=status.HTTP_404_NOT_FOUND)

        count = AddOrCancelRequest.objects.all().delete()
        if count[0] is not 0:
            return JsonResponse({'message': '{} AddOrCancelRequests were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({"message":"No Data found for the current Request"})

