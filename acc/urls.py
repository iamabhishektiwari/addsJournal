from django.conf.urls import url,include
from acc import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    #user auth urls
    url(r'^login/$', views.login),
	url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid_login),

    #registrations
    url(r'^register/$', views.register_user),
    url(r'^register_success/$', views.register_success),

 ]
