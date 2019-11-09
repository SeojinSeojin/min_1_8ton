from django.contrib import admin
from django.urls import path
import min1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', min1.views.home, name='home'),
]
