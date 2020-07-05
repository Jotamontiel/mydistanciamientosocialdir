from django.urls import path
from .views import HomePageView, AboutPageView, DisplayPageView, MapDisplayView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('home/<int:idcategory>', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('display/', DisplayPageView.as_view(), name="display"),
    path('map_display/', MapDisplayView.as_view(), name="map_display"),
]