from django.conf.urls import url
from users import api as users_api

urlpatterns = [
    url(r'^get_auth_token/$', users_api.AuthToken.as_view(), name='register_user'),
    url(r'^register/$', users_api.Register.as_view(), name='auth_token'),
    url(r'^authenticate/$', users_api.AuthenticateUser.as_view(), name='auth_token'),
]