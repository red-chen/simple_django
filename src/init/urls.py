from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^my_server/', include('servers.my_server.urls')),
    url(r'^', include('servers.ag_server.urls')),
]
