from rest_framework.decorators import api_view
from .models import Order, Post, Employee
from . import serializers
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET'])
def read_orders(_, **kwargs):
    pk = kwargs.get('pk', None)
    if pk is not None:
        try:
            order = Order.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        orders = Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE'])
def create_edit_delete_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = serializers.OrderSerializer(order, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def read_posts(_, **kwargs):
    pk = kwargs.get('pk', None)
    if pk is not None:
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        posts = Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE'])
def create_edit_delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = serializers.PostSerializer(post, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def read_employees(_, **kwargs):
    pk = kwargs.get('pk', None)
    if pk is not None:
        try:
            employee = Employee.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        employees = Employee.objects.all()
        serializer = serializers.EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE'])
def create_edit_delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = serializers.EmployeeSerializer(employee, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
