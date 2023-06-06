from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import *

@api_view(['GET'])
def productsView(request):
    data    = Product.objects.filter(owner=request.user)
    print(data)
    
    ser     = ProductSerializer(data, many=True) 
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def productView(request, product_id):
    data    = Product.objects.get(pk=product_id)
    return True
@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()

        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def servicesList(request, title=None, description=None):
    if request.method == 'GET':  
        data = Services.objects.all()
        serializer = ServicesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = Services()   
        data.title = title
        data.description = description
        data.save()

        return Response(status=status.HTTP_201_CREATED)  
@api_view(['GET', 'DELETE'])    
def service(request, service_title):
    service_title.lower()
    print(service_title)
    try:
        data = Services.objects.get(title=service_title)
        print(data)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serailizer = ServicesSerializer(data, context={'request': request}, many=True)
        return Response(serailizer.data)
    
    else :
        if request.method == 'DELETE':
            try:
                data.delete()
            except:
                pass    
            return Response(status=status.HTTP_200_OK)
    