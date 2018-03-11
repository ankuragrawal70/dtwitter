from rest_framework import serializers
from dweets.models import Dweet, Comments, Likes


class BaseSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		try:
			instance = self.Meta.model(**validated_data)
			instance.save()
		except Exception as e:
			raise Exception(e)
		return instance


class DweetSerializer(BaseSerializer):
	class Meta:
		model = Dweet
		fields = '__all__'


class DweetLikesSerializer(BaseSerializer):
	class Meta:
		model = Likes
		fields = '__all__'


class DweetCommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields = '__all__'
