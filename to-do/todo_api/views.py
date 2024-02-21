from django.http import JsonResponse
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .send_sms import sms_sender
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
        
         # Send SMS when a new order is added
        message = "New order added: {} - {}".format(serializer.data['item'], serializer.data['amount'])
        recipients = ["+254726015886"]  # Replace with the recipient's phone number
        sender = "40563"  # Replace with your sender ID or short code
        sms_sender.send(message, recipients, sender)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT'])
def customer_detail(request, id):

    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT'])
def order_detail(request, id):

    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
