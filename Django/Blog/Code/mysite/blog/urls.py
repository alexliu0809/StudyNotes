from django.conf.urls import url
from . import views

urlpatterns = [

	# Navigate to post_list if no para
	# First para: url pattern
	# Second para: the view to open, the view is defined in views.py
	# name the url

	# First pattern doesn't pass para
	url(r'^$', views.post_list, name = 'post_list'),
	# Second gives one para
	url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,name='post_list_by_tag'),

	# Navigate to detail if year+month+day+postinfo
	# Name of this url is 'post_detail'
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
	views.post_detail,
	name = 'post_detail'),
	
	url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]