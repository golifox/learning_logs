from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myapi.views import *

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)


urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),

    # API URLs
    #path('', include('myapi.urls')),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Models URLs
    path('', include('blog.urls')),
    path('', include('users.urls')),
]
