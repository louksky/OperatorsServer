from django.urls import include, path
from rest_framework import routers
from authapp import views 
from api_eng_ import urls as api_urls_site
app_name = 'authapp'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
    path('api_eng/', include(api_urls_site, namespace='api_eng_')),
]