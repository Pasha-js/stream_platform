
from django.contrib import admin
from django.urls import path
from project import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.index, name='index' ),
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns = [
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)