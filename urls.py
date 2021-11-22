from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = ''
admin.site.site_title = ''
admin.site.index_title = ''

urlpatterns = [



    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('accounts.urls', namespace='account')),
    re_path(r'^assess/', include('check.urls', namespace='check')),



   
]










if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
