from django.contrib import admin
from .models import Country, Product, MarketData, UserPreference


# Customize the admin interface and register the models created

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')  # Display these fields in the list view
    search_fields = ('name',)  # Enable search by country name

admin.site.register(Country, CountryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  
    search_fields = ('name', 'category')

admin.site.register(Product, ProductAdmin)

class MarketDataAdmin(admin.ModelAdmin):
    list_display = ('country', 'product', 'year', 'value')  
    list_filter = ('country', 'product', 'year')  # Filter by these fields
    search_fields = ('country__name', 'product__name')  

admin.site.register(MarketData, MarketDataAdmin)

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference')  # Assuming these fields exist
    search_fields = ('user__username', 'preference')  # Search by username and preference

admin.site.register(UserPreference, UserPreferenceAdmin)