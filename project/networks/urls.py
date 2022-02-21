
from django.urls import path
from .views import *

urlpatterns = [




    path('', NetworkView.as_view(), name='network'),
    path('haha', external, name='ext'),

    path('apache-access-log', apache_access_log, name='apache-access-log'),
    path('apache-error-log', apache_error_log, name='apache-error-log'),

    path('trace-route', trace_route, name='trace-route'),
    path('trace-route-request', trace_route_request, name='trace-route-request'),

    path('nmapper', nmapper, name='nmapper')
]