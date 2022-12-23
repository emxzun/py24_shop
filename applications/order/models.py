from django.contrib.auth import get_user_model
from django.db import models
from applications.product.models import Product
import uuid

User = get_user_model()


class Order(models.Model):
    ORDER_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),
        ('declined', 'declined')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=30, choices=ORDER_STATUS, null=True, blank=True)
    is_confirm = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    address = models.TextField()
    number = models.CharField(max_length=30)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activation_code = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    # def create_activation_code(self):
    #     import uuid
    #     code = str(uuid.uuid4())
    #     self.activation_code = code
    #
    def save(self, *args, **kwargs):
        self.total_price = self.amount * self.product.price
        return super().save(*args, **kwargs)
