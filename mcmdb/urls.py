
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', 'index', name='index'),
    url(r'^asset/', include('asset.urls')),
]
