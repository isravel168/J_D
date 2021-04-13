from django.conf.urls import url
from . import views
from .views import login
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 24-03-2021

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 25-03-2021



#sales lead
    url('token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    url('token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'),

    url(r'^login/', login),  # SalesLeadListView.as_view()),


#08-04-2021


]