from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from dweets import services
from users.authentication import UserTokenAuthentication


class AddTweet(APIView):
	"""
		View to add new Tweet
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: Response of a tweet content add request.
		all the validations are checked if tweet content and user is valid.
		"""
		user_profile = request.user.profile
		dweet_content = request.POST['dweet_content']
		ser = self.service_class(dweet_content=dweet_content, user_profile=user_profile)
		response = ser.validate_and_add_dweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class LikeTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		user_profile = request.user.profile
		dweet_id = request.POST['dweet_id']
		ser = self.service_class(dweet_id=dweet_id, user_profile=user_profile)
		response = ser.like_tweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class CommentsTweet(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		user_profile = request.user.profile
		dweet_id = request.POST['dweet_id']
		comment = request.POST['comment_text']
		ser = self.service_class(dweet_id=dweet_id, user_profile=user_profile, comment_text=comment)
		response = ser.add_comment_on_tweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class SearchTweets(APIView):
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

