from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'msi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'disease.views.index'),
    (r'^addone/$', "disease.views.addinteraction"),
    (r'^addmany/$', "disease.views.addinteractiongroup"),
    (r'^getall/$', "disease.views.getall"),
    (r'^getdetails/$', "disease.views.getdetails"),
    (r'^getallsince/$', "disease.views.getallsince"),
    (r'^getdetailssince/$', "disease.views.getdetailssince"),
    (r'^time/$', "disease.views.time"),
)
