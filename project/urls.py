"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/' , include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('rooms/',include('property.urls',namespace='rooms')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('post/',include('blog.urls',namespace='posts')),
    path('about/',include('about.urls',namespace='about')),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('index.urls',namespace='home')),
    path('contact/',include('contact.urls',namespace='contact')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup', include('rest_auth.registration.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

