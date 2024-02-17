from django.http import JsonResponse
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

# class CustomerListCreate(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class OrderListCreate(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# get all customers and orders
# serialize them
# return json
def customer_list(request):
    # get customers
    customers = Customer.objects.all()
    # serialize all customers
    serializer = CustomerSerializer(customers, many = True)
    return JsonResponse(serializer.data)