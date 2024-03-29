from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.item} - {self.customer.name if self.customer else 'Unknown'}"