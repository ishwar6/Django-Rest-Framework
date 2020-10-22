from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'Wisfrags Education Private Limited - BlissedMaths SuperAdmin Panel'
admin.site.site_title = 'Wisfrags Education'
admin.site.index_title = 'Managed by Gaurav Malhotra, Pankaj Kumar & Ishwar Jangid'

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
