from django.conf.urls import include, url

import servers.my_server.views as my_server_views

urlpatterns = [
    url(r'^html/$', my_server_views.HtmlView.as_view()),
    url(r'^$', my_server_views.IndexView.as_view()),
]
