

from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('api_schema',get_schema_view(title='Food Delivery API',description='Food delivery API '),name='api_schema'),
    path('index/', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('delivery.urls')),
    
]
