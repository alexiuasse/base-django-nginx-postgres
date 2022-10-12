from django.contrib import admin
from django.urls import path, include
from django.views.defaults import server_error

from .views import test_send_email


urlpatterns = [
    path("__debug__/", include('debug_toolbar.urls')),
    path("admin/", admin.site.urls),

    path("test/error/500/", server_error),
    path("test/sendemail/", test_send_email),
]
