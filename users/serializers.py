from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models, transaction
from users.models import UserProfile


class UserAlreadyExistsExceptions(Exception):
	pass


class UserSerializer(serializers.ModelSerializer):
	email = models.EmailField(unique=True, error_messages={
		'unique': "A user with that email already exists.",
	},)
	
	def to_internal_value(self, data):
		result = super(UserSerializer, self).to_internal_value(data)
		result['email'] = result['username']
		return result
	
	def create(self, validated_data):
		with transaction.atomic():
			"""
			creating user and profile instance
			"""
			res = super(UserSerializer, self).create(validated_data)
			res.set_password(validated_data['password'])
			res.save()
			
			profile = UserProfile.objects.create(user_id=res.id)
			return profile
			
	class Meta:
		model = (User)
		fields = '__all__'

