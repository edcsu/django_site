from django.conf.urls import include, url
# from django.contrib import admin
from sprof import views

urlpatterns = [
    # Examples:
     url(r'^$', 'sprof.views.index', name='index'),
     url(r'^contact/$', 'sprof.views.contacts', name='contact'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
]
