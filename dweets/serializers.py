from rest_framework import serializers
from dweets.models import Dweet, Comments, Likes
from utils.validators import SimpleTweetValidator
import traceback


class DweetSerializer(serializers.ModelSerializer):
	content = serializers.CharField(
		max_length=100, validators=[SimpleTweetValidator],
		help_text="Please enter a valid tweet of maximum 100 length character",
		allow_blank=False,
		error_messages={
			'unique': "A tweet aleady exists.",
		},
	)
	
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
