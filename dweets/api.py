from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from dweets import services
from users.authentication import UserTokenAuthentication


class AddTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		user_profile = request.user.profile
		tweet_content = request.POST['tweet_content']
		ser = self.service_class(tweet_content=tweet_content, user_profile=user_profile)
		response = ser.validate_and_add_dweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class LikeTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class CommentsTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)


class SearchTweets(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

