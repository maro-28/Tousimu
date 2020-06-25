from django.urls import path
from . import views

app_name = 'simulators'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('funded-simulator', views.FundedSimulatorView.as_view(),
         name="funded-simulator"),
    path('dividend-simulator', views.DividendSimulatorView.as_view(),
         name="dividend-simulator"),
    path('flat-price-sale', views.FlatPriceSaleView.as_view(),
         name="flat-price-sale"),
]
