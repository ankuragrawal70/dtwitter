from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.authentication import UserTokenAuthentication


class AddTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	


class LikeTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class CommentsTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class SearchTweets(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

