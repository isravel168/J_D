from django.conf.urls import url
from .views import jobPosting
from user.api.views import myJobDescription, userProfile

urlpatterns = [
        url(r'^userprofile/$', userProfile),  # SalesLeadListView.as_view()),
        url(r'^userprofile/(?P<pk>[-\w]+)', userProfile),  # SalesLeadDetailView.as_view()),
        url(r'^userprofile/$', userProfile),  # SalesLeadCreateApi.as_view()),
        url(r'^userprofile/(?P<pk>[-\w]+)', userProfile),  # SalesLeadUpdateApi.as_view()),
        url(r'^userprofile/(?P<pk>[-\w]+)', userProfile),  # SalesLeadDeleteApi.as_view())

        url(r'^jobdescription/$', myJobDescription),  # SalesLeadListView.as_view()),
        url(r'^jobdescription/(?P<pk>[-\w]+)', myJobDescription),  # SalesLeadDetailView.as_view()),
        url(r'^jobdescription/$', myJobDescription),  # SalesLeadCreateApi.as_view()),
        url(r'^jobdescription/(?P<pk>[-\w]+)', myJobDescription),  # SalesLeadUpdateApi.as_view()),
        url(r'^jobdescription/(?P<pk>[-\w]+)', myJobDescription),  # SalesLeadDeleteApi.as_view())

        url(r'^jobposting/$', jobPosting),  # SalesLeadListView.as_view()),
        url(r'^jobposting/(?P<pk>[-\w]+)', jobPosting),  # SalesLeadDetailView.as_view()),
        url(r'^jobposting/$', jobPosting),  # SalesLeadCreateApi.as_view()),
        url(r'^jobposting/(?P<pk>[-\w]+)', jobPosting),  # SalesLeadUpdateApi.as_view()),
        url(r'^jobposting/(?P<pk>[-\w]+)', jobPosting),  # SalesLeadDeleteApi.as_view())
]