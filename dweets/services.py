from dweets.dto import SerializedResponse
from users import services as users_services
from dweets.serializers import DweetSerializer
from dweets import models as dweet_models

class DweetService(object):
	"""
	Service just to validate and add tweet
	if user and tweet is valid, it can be added to the user's tweet list
	"""
	serializer = DweetSerializer
	
	def __init__(self, dweet_content=None, dweet_id=None, user_id=None, user_profile=None):
		self.dweet_content = dweet_content
		self.dweet_id = dweet_id
		self.user = self.get_user_profile(user_id, user_profile)
	
	@staticmethod
	def get_user_profile(user_id=None, user_profile=None):
		assert (user_id or user_profile), "user id or profile required"
		if user_profile:
			return user_profile
		return users_services.get_user_profile(user_id)
	
	def validate_and_add_dweet(self):
		"""
		:return:
		if dweet is valid to be added then new dweet will be added else error will be generated
		and response object will be returned with the state(success, data and errors)
		"""
		ser_ins = self.serializer(data={"created_by": self.user.id, 'content': self.dweet_content})
		response = SerializedResponse()
		if ser_ins.is_valid():
			try:
				response.data = ser_ins.create(ser_ins.validated_data)
				response.success = True
			except Exception as e:
				response.errors = str(e)
		else:
			response.errors = ser_ins.errors
		return response
	
	def add_likes(self):
		assert self.dweet_id, "Please gave a tweet to be liked"
		get_dweet =  get_dweet_from_dweet_id(self.dweet_id)
		
		
def get_dweet_from_dweet_id(dweet_id):
	return dweet_models.Dweet.objects.get(id=dweet_id)