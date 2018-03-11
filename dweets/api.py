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
		:return: success and failure response based on:
					if dweet is added successfully or not
					data contains Dweet info
		
		"""
		user_profile = request.user.profile
		dweet_content = request.POST.get('dweet_content', "")
		ser = self.service_class(dweet_content=dweet_content, user_profile=user_profile)
		response = ser.validate_and_add_dweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class LikeTweet(APIView):
	"""
	View to add like on a tweet
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		"""
				:param request:
				:param args:
				:param kwargs:
				:return: success and failure response based on:
					if dweet is liked successfully or not
					data contains Dweet info with current liked info
		"""
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
	"""
	View to add comments or tweets
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	service_class = services.DweetService
	
	def post(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: success and failure response based on:
			if comment is posted successfully or not
			data contains dweet info with current posted comment info
		"""
		user_profile = request.user.profile
		dweet_id = request.POST.get('dweet_id')
		comment = request.POST.get('comment_text', '')
		ser = self.service_class(dweet_id=dweet_id, user_profile=user_profile, comment_text=comment)
		response = ser.add_comment_on_tweet()
		return Response({
			'success': response.get_success(),
			'errors': response.get_errors(),
			'data': response.get_data()}
		)


class SearchTweets(APIView):
	"""
	View to search a tweet with particular search string
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: return list of tweets search for a particular substring-
		if no tweet exits blank list is returned
		if substring is not valid, error is returned
		if q=* is supplied then all tweets are returned
		"""
		search_str = request.GET.get('q')
		response = services.DweetService(user_profile=request.user.profile).search_tweets(search_str)
		return Response({
			"success": response.get_success(),
			"data": response.get_data(),
			'errors': response.get_errors()}
		)

