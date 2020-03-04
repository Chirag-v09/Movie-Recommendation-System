from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
]
