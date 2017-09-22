from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'ticksys'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'ticksys/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'ticksys/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/profile_edit/$', views.profile_edit, name='profile_edit'),
    url(r'^warning/$', views.warning, name='warning'),
    url(r'^dashboard/create_ticket/$', views.CreateTicket.as_view(), name='create_ticket'),
    url(r'^dashboard/(?P<pk>[0-9]+)/$', views.ticket_detail, name='ticket_detail'),
    url(r'^dashboard/(?P<pk>[0-9]+)/edit_ticket/$', views.EditTicket.as_view(), name='edit_ticket')
]