from django import forms
from .models import Country, Product, UserPreference

'''This form allows users to select multiple countries and products, and 
choose a start and end date for the data range'''

class MarketDataForm(forms.Form):
    country = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=False
    )
    end_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=False
    )

    # Form to allow users to set their preferences

class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['favorite_country', 'favorite_product', 'visualization_type', 'enable_notifications', 'notification_frequency']
        widgets = {
            'favorite_country': forms.Select(),
            'favorite_product': forms.Select(),
            'visualization_type': forms.RadioSelect,
            'notification_frequency': forms.Select
        }
