from django.contrib import admin
from django.urls import path, include

from accounts.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compte/nouveau/', signup, name="signup")
]
