from django.conf.urls import patterns, include, url
from django.contrib import admin
from adddata.views import add_dinner


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add-name/$','adddata.views.add_dinner'),
    url(r'^thanks/$','adddata.views.thanks'),
    url(r'^register/$', 'userAuth.views.register', name='register'),
    url(r'^login/$', 'userAuth.views.login', name='login'),
    url(r'^index/$', 'userAuth.views.index', name='index'),
    url(r'^log-out/$', 'userAuth.views.logOut', name='logOut')


)
