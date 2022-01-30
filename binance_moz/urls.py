from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import binance_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', binance_app.views.home, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('binance_app/', include('binance_app.urls'))
]
