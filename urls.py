from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # My Example:
    # (r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail')
    # (r'^articles/(?P<year>\d{4})/$', 'news.views.year_archive'),
    # if more urlpatterns defined, use +=
    # adding urlpatterns from other files: 
    # (r'^weblog/', include('django_website.apps.blog.urls.blog')),
    # (r'^credit/', include(extrapatterns))
    # (r'^blog/(?P<year>\d{4})/$', 'year_archive', {'foo': 'bar'})
    
    # (r'^polls/$', 'index'),
    # (r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    # (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    # (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
    (r'^polls/', include('eVirtuve.polls.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', 'eVirtuve.polls.views.http404')
)
