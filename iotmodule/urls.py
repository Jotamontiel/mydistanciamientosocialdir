from django.urls import path
from .views import IotModuleView, DeviceListView, DeviceDetailView, DeviceCreate, DeviceUpdate, DeviceDelete

iotmodule_patterns = ([
    path('', IotModuleView.as_view(), name='iotmodule'),
    path('device_list/', DeviceListView.as_view(), name='devices'),
    path('device_detail/<int:pk>/<slug:slug>/', DeviceDetailView.as_view(), name='device'),
    path('device_create/', DeviceCreate.as_view(), name='device_create'),
    path('device_update/<int:pk>/<slug:slug>/', DeviceUpdate.as_view(), name='device_update'),
    path('device_delete/<int:pk>/', DeviceDelete.as_view(), name='device_delete'),
], 'iotmodule')