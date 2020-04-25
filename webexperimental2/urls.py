"""webexperimental2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from iotmodule.urls import iotmodule_patterns

urlpatterns = [
    # Display, Base, Home, About paths
    path('', include('core.urls')),
    # Services path
    path('', include('services.urls')),
    # Courses path
    path('', include('courses.urls')),
    # Pages path
    path('pages/', include(pages_patterns)),
    # Contact path
    path('', include('contact.urls')),
    # IotModule path
    path('iotmodule/', include(iotmodule_patterns)),
    # Profiles path
    path('profiles/', include(profiles_patterns)),
    # Admin path
    path('admin/', admin.site.urls),
    # Auth paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom titles for admin
admin.site.site_header = "IOT CHILE CO."
admin.site.index_title = "PANEL DE ADMINISTRACIÓN"
admin.site.site_title = "IOT CHILE CO."