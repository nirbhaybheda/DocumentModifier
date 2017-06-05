from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

from views import ModifyFile

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docxmodifier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/modify$', ModifyFile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
