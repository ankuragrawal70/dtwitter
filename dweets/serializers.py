from rest_framework import serializers
from dweets.models import Dweet, Comments, Likes


class BaseSerializer(serializers.ModelSerializer):
	"""
	Base serializer which override create method and raise exceptions if found
	"""
	def create(self, validated_data):
		try:
			instance = self.Meta.model(**validated_data)
			instance.save()
		except Exception as e:
			raise Exception(e)
		return instance


class DweetSerializer(BaseSerializer):
	"""
	Dweet model serializer to validate and create Dweet model info
	"""
	class Meta:
		model = Dweet
		fields = '__all__'
	
	def to_representation(self, instance):
		ret = super(BaseSerializer, self).to_representation(instance)
		ret['created_by'] = instance.created_by.user.email
		return ret
		
	
class DweetLikesSerializer(BaseSerializer):
	"""
		Dweet model serializer to validate and create Likes model info
		"""
	class Meta:
		model = Likes
		fields = '__all__'


class DweetCommentsSerializer(serializers.ModelSerializer):
	"""
		Dweet model serializer to validate and create Comments model info
	"""
	class Meta:
		model = Comments
		fields = '__all__'
