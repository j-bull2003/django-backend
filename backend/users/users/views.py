from django.http import JsonResponse
from .models import Users, Occupations
from .serializers import UsersSerializer, OccupationsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','HEAD', 'POST'])
def users_list(request, format=None):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method == 'HEAD':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def occupations_list(request, format=None):
    if request.method == 'GET':
        occupations = Occupations.objects.all()
        serializer = OccupationsSerializer(occupations, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = OccupationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def users_detail(request, id, format=None):

    # try:
    users = Users.objects.get(pk=id)
    # except users.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsersSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = UsersSerializer(users, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)