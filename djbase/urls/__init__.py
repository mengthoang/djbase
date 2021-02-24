from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('allauth.urls')),
    path('avatar/', include('avatar.urls')),
    
    path('api/v1/', include('djbase.urls.api_v1')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
