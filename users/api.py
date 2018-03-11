from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from users import services as user_services
from users.authentication import UserTokenAuthentication


class Register(APIView):
	"""
	API view to register a user
	"""
	def post(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: success or failure based on:
		    success if user Registration is successful
		    else error is returned
		"""
		username = request.POST.get('username')
		password = request.POST.get('password')
		success, error = user_services.RegisterAuthenticateService.create_user(username=username, password=password)
		if success:
			return Response({'success': success, 'msg':'User Created Successfully'})
		else:
			return Response({'success': success, 'msg': error})


class AuthenticateUser(APIView):
	"""
	API view to authenticate user
	"""
	def post(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: success is user is authenticated
			else error
		"""
		username = request.POST.get('username')
		password = request.POST.get('password')
		success, error = user_services.RegisterAuthenticateService.authenticate_user(username=username, password=password)
		if success:
			return Response({'success': success, 'msg':'User is authenticated successfully'})
		else:
			return Response({'success': success, 'msg': error})


class AuthToken(APIView):
	def post(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return: return auth token to user which have some expiry time set in setting.py
		"""
		username = request.POST.get('username')
		password = request.POST.get('password')
		token_service = user_services.TokenAuthenticateService()
		result_data = token_service.get_or_create_token(username, password)
		if 'token' in result_data:
			result_data['token'] = result_data['token'].key
		return Response(result_data)


class SearchTweeter(APIView):
	"""
	API view to search dweeter
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	

class FollowTweeter(APIView):
	"""
	API view to follow dweeter
	"""
	authentication_classes = (UserTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
