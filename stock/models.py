from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.ticker_symbol})"