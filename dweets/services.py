from dweets.dto import SerializedResponse
from users import services as users_services
from dweets.serializers import DweetSerializer, DweetLikesSerializer, DweetCommentsSerializer
from dweets import models as dweet_models


class DweetService(object):
	"""
	Service just to validate and add tweet
	if user and tweet is valid, it can be added to the user's tweet list
	"""
	serializer = DweetSerializer
	liked_serializer = DweetLikesSerializer
	comments_serializer = DweetCommentsSerializer
	
	def __init__(
		self, dweet_content=None,
		dweet_id=None,
		user_id=None,
		user_profile=None,
		comment_text=None,
		comment_id=None
	):
		self.dweet_content = dweet_content
		self.dweet_id = dweet_id
		self.user = self.get_user_profile(user_id, user_profile)
		self.comment_text = comment_text
		self.comment_id = comment_id
	
	@staticmethod
	def get_user_profile(user_id=None, user_profile=None):
		assert (user_id or user_profile), "user id or profile required"
		if user_profile:
			return user_profile
		return users_services.get_user_profile(user_id)
	
	def __get_response(self, serializer_instance):
		response = SerializedResponse()
		if serializer_instance.is_valid():
			try:
				response.data = serializer_instance.create(serializer_instance.validated_data)
				response.success = True
			except Exception as e:
				response.errors = str(e)
		else:
			response.errors = serializer_instance.errors
		return response
	
	def validate_and_add_dweet(self):
		"""
		:return:
		if dweet is valid to be added then new dweet will be added else error will be generated
		and response object will be returned with the state(success, data and errors)
		"""
		ser_ins = self.serializer(data={"created_by": self.user.id, 'content': self.dweet_content})
		return self.__get_response(ser_ins)
		
	def like_tweet(self):
		assert self.dweet_id, "Please gave a tweet to be liked"
		ser_ins = self.liked_serializer(data={'dweet': self.dweet_id, 'liked_by': self.user.id})
		return self.__get_response(ser_ins)
	
	def add_comment_on_tweet(self):
		assert self.dweet_id, "Please gave a tweet to be liked"
		ser_ins = self.comments_serializer(data={
			'dweet': self.dweet_id, 'commented_by': self.user.id,
			'content': self.comment_text})
		return self.__get_response(ser_ins)

