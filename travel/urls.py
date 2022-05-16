from django.contrib import admin
from django.urls import path, include

from travel import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
    path('users/', include('users.urls')),
    path('trip/', include('trip.urls')),
    path('place/', include('place.urls'))
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
