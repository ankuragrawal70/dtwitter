from django.conf.urls import url
from dweets import api as dweets_api
app_name = 'dweets'
urlpatterns = [
    url(r'^add-tweet/$', dweets_api.AddTweet.as_view(), name='add_tweet'),
    url(r'^like-tweet/$', dweets_api.LikeTweet.as_view(), name='like_tweet'),
    url(r'^add-comment/$', dweets_api.CommentsTweet.as_view(), name='like_tweet'),
]