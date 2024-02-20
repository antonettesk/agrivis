"""
URL configuration for agrivis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from market.views import home
from market.views import home, qcl_data_view, qv_data_view, pp_data_view, fbs_data_view, ti_data_view, market_data_view, market_data_form_view, user_preferences_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns = [
    path('', home, name='home'),
    path('market-data/Crops and Livestock Products/', qcl_data_view, name='qcl_data'),
    path('market-data/Value of Agricultural Production/', qv_data_view, name='qv_data'),
    path('market-data/Producer Prices/', pp_data_view, name='pp_data'),
    path('market-data/Food Balance Sheets/', fbs_data_view, name='fbs_data'),
    path('market-data/Trade Indices/', ti_data_view, name='ti_data'),
    path('market-data/view/', market_data_view, name='market_data'),
    path('market-data/form/', market_data_form_view, name='market_data_form'),
    path('user-preferences/', user_preferences_view, name='user_preferences'),
]