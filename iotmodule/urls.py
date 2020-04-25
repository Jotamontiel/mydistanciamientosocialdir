from django.urls import path
from .views import IotModuleView

iotmodule_patterns = ([
    path('', IotModuleView.as_view(), name='iotmodule'),
], 'iotmodule')