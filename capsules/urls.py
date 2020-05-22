from django.urls import path
from .views import CapsuleListView, CapsuleDetailView, CapsuleCreate, CapsuleUpdate, CapsuleDelete

capsules_patterns = ([
    path('', CapsuleListView.as_view(), name='capsules'),
    path('<int:pk>/<slug:slug>/', CapsuleDetailView.as_view(), name='capsule'),
    path('create/', CapsuleCreate.as_view(), name="create"),
    path('update/<int:pk>/', CapsuleUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', CapsuleDelete.as_view(), name='delete'),
], 'capsules')