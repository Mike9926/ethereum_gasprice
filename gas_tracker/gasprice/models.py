from django.db import models

# Create your models here.
class GasPrice(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    gas_price = models.FloatField()
    transaction_speed = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.gas_price} Gwei"