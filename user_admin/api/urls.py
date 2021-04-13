from django.conf.urls import url

from user_admin.api.views import requestForCancelPlan, addLicense, reduceLicense
from user.api.views import userProfile

urlpatterns = [
    url(r'^usermaster/$', userProfile),  # SalesLeadListView.as_view()),
    url(r'^usermaster/(?P<pk>[-\w]+)',userProfile),  # SalesLeadDetailView.as_view()),
    url(r'^usermaster/$',userProfile),  # SalesLeadCreateApi.as_view()),
    url(r'^usermaster/(?P<pk>[-\w]+)',userProfile),  # SalesLeadUpdateApi.as_view()),
    url(r'^usermaster/(?P<pk>[-\w]+)',userProfile),  # SalesLeadDeleteApi.as_view())

    url(r'^adduser/$', addLicense),  # SalesLeadListView.as_view()),
    url(r'^adduser/(?P<pk>[-\w]+)', addLicense),  # SalesLeadDetailView.as_view()),
    url(r'^adduser/$', addLicense),  # SalesLeadCreateApi.as_view()),
    url(r'^adduser/(?P<pk>[-\w]+)', addLicense),  # SalesLeadUpdateApi.as_view()),
    url(r'^adduser/(?P<pk>[-\w]+)', addLicense),  # SalesLeadDeleteApi.as_view())

    url(r'^reduceuser/$', reduceLicense),  # SalesLeadListView.as_view()),
    url(r'^reduceuser/(?P<pk>[-\w]+)', reduceLicense),  # SalesLeadDetailView.as_view()),
    url(r'^reduceuser/$', reduceLicense),  # SalesLeadCreateApi.as_view()),
    url(r'^reduceuser/(?P<pk>[-\w]+)', reduceLicense),  # SalesLeadUpdateApi.as_view()),
    url(r'^reduceuser/(?P<pk>[-\w]+)', reduceLicense),  # SalesLeadDeleteApi.as_view())

    url(r'^cancelplan/$', requestForCancelPlan),  # SalesLeadListView.as_view()),
    url(r'^cancelplan/(?P<pk>[-\w]+)', requestForCancelPlan),  # SalesLeadDetailView.as_view()),
    url(r'^cancelplan/$', requestForCancelPlan),  # SalesLeadCreateApi.as_view()),
    url(r'^cancelplan/(?P<pk>[-\w]+)', requestForCancelPlan),  # SalesLeadUpdateApi.as_view()),
    url(r'^cancelplan/(?P<pk>[-\w]+)', requestForCancelPlan),  # SalesLeadDeleteApi.as_view())

]
