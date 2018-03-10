from rest_framework.authentication import TokenAuthentication
from users.services import TokenAuthenticateService
from rest_framework import exceptions


class UserTokenAuthentication(TokenAuthentication):
	def authenticate_credentials(self, key):
		user, token = super(UserTokenAuthentication, self).authenticate_credentials(key)
		if TokenAuthenticateService.is_token_expired(token):
			raise exceptions.AuthenticationFailed('Your token is expired')
		return user, token