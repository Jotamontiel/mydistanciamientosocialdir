from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete, NewspaperDisplayView, PageVideoCreate, PageImageCreate, PageVideoUpdate, PageImageUpdate, PageVideoListView, PageImageListView, PageVideoDelete, PageImageDelete

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('video_list/<int:pk>/', PageVideoListView.as_view(), name='videos'),
    path('image_list/<int:pk>/', PageImageListView.as_view(), name='images'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('video_create/', PageVideoCreate.as_view(), name='video_create'),
    path('image_create/', PageImageCreate.as_view(), name='image_create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('video_update/<int:pk>/<int:pageid>/', PageVideoUpdate.as_view(), name='video_update'),
    path('image_update/<int:pk>/<int:pageid>/', PageImageUpdate.as_view(), name='image_update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete' ),
    path('video_delete/<int:pk>/', PageVideoDelete.as_view(), name='video_delete'),
    path('image_delete/<int:pk>/', PageImageDelete.as_view(), name='image_delete'),
    path('newspaper_display/<int:pk>/<slug:slug>/', NewspaperDisplayView.as_view(), name="newspaper_display"),
], 'pages')