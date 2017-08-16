from django.conf.urls import include, url
from django.contrib import admin
from odp_demo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'odp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^odp/', include('odp_demo.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
