from users import services as users_services


class DweetService():
	
	def __init__(self, user_id=None, user_profile=None):
		self.user = self.__get_user_profile(user_id, user_profile)
		
	def __get_user_profile(self, user_id=None, user_profile=None):
		assert (user_id or user_profile), "user id or profile required"
		if user_profile:
			return user_profile
		return users_services.get_user_profile(user_id)
		
	def validate_and_add_dweet(self, tweet_content):
		pass
	
	def delete_dweet(self, profile_id):
		pass
