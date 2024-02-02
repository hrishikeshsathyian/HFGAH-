
from django.urls import path, include
from . import views

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
    path('volunteer', include('volunteer.urls')),
]