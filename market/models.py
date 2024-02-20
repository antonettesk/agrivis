from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MarketData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    value = models.FloatField()
    unit = models.CharField(max_length=50)

    class Meta:
        unique_together = ('country', 'product', 'year')

    def __str__(self):
        return f"{self.product.name} in {self.country.name} ({self.year})"

# Preferences model for data visualization and notification settings

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_countries = models.ManyToManyField(Country)
    favorite_products = models.ManyToManyField(Product)
    visualization_type = models.CharField(max_length=100, choices=(('bar', 'Bar Chart'), ('line', 'Line Chart'), ('pie', 'Pie Chart')), default='bar')
    enable_notifications = models.BooleanField(default=True)
    notification_frequency = models.CharField(max_length=50, choices=(('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')), default='weekly')

    def __str__(self):
        return f"{self.user.username}'s Preferences"