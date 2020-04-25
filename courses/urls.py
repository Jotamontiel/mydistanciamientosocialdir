from .views import CoursesListView, CoursesDetailView
from django.urls import path

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('courses/<int:idcategory>', CoursesListView.as_view(), name='courses'),
    path('<int:pk>/<slug:slug>/', CoursesDetailView.as_view(), name='course'),
]