from django.http import JsonResponse
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# class CustomerListCreate(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class OrderListCreate(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# get all customers and orders
# serialize them
# return json

@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        # get customers
        customers = Customer.objects.all()
        # serialize all customers
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({'customers': serializer.data})
    
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({'orders':serializer.data})
    
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)