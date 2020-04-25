from django.urls import path
from .views import HomePageView, AboutPageView, DisplayPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('home/<int:idcategory>', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('display/', DisplayPageView.as_view(), name="display"),
]