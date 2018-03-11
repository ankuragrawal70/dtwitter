from rest_framework import serializers
from dweets.models import Dweet, Comments, Likes
from utils.validators import SimpleTweetValidator
import traceback


class DweetSerializer(serializers.ModelSerializer):
	
	def create(self, validated_data):
		try:
			instance = self.Meta.model(**validated_data)
			instance.save()
		except Exception as e:
			raise Exception(e)
		return instance
	
	class Meta:
		model = Dweet
		fields = '__all__'
