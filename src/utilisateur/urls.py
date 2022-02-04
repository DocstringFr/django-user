from django.contrib import admin
from django.urls import path, include

from accounts.views import home, signup, profile, login, logout

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
]