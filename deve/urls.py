from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve


urlpatterns = [
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('compte/', include('users.urls')),
    path('admin/', admin.site.urls),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

