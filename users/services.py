from users.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.utils import timezone
from dtwitter import constants
from users.models import UserProfile


class RegisterAuthenticateService(object):
	serializer_class = UserSerializer
	
	@classmethod
	def create_user(cls, username, password):
		"""
		:param username:
		:param password:
		:return: if username and password are valid (no other user exists of the same email).
		We will create a valid user
		"""
		serializer_ins = cls.serializer_class(data={'username':username, 'password': password})
		success, error = False, ''
		if serializer_ins.is_valid():
			try:
				serializer_ins.create(serializer_ins.validated_data)
				success = True
			except Exception as e:
				error = str(e)
		else:
			error = serializer_ins.errors
		return success, error
	
	@staticmethod
	def authenticate_user(username, password):
		"""
		:param username:
		:param password:
		:return: authenticate username and password
		"""
		user_ins = authenticate(username=username, password=password)
		if user_ins:
			return True, ''
		else:
			return False, 'invalid credential'
	

class TokenAuthenticateService(object):
	serializer_class = AuthTokenSerializer
	expiration_seconds = constants.TOKEN_EXPIRY_TIME_IN_SECONDS
	
	def get_or_create_token(self, username, password):
		success, errors = False, ''
		result_data = {'success': success}
		ser_ins = self.serializer_class(data={'username':username, 'password':password})
		if ser_ins.is_valid():
			# get or create token
			token, created = Token.objects.get_or_create(user=ser_ins.validated_data['user'])
			if not created:
				if self.is_token_expired(token):
					token.delete()
					token = Token.objects.create(user=ser_ins.validated_data['user'])
			result_data.update({'token':token})
		else:
			result_data.update({'errors': ser_ins.errors})
		return result_data

	@classmethod
	def is_token_expired(cls, token):
		token_creation_time = token.created
		time_gap = timezone.now() - token_creation_time
		if time_gap.seconds >= cls.expiration_seconds:
			return True
		return False
	
	
def get_user_profile(user_id):
	try:
		return UserProfile.objects.get(id=user_id)
	except Exception as e:
		print("exception occurred", str(e))
		return None