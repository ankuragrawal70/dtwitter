from django.db import models
from datetime import datetime

from utils.managers import BaseManager


class BaseModel(models.Model):
	"""
	Abstract Base model containing timestamp and active status fields.
	This model can be inherited in every other model to reuse
	the time stamp and active status
	"""
	created_date = models.DateTimeField(editable=False)
	modified_date = models.DateTimeField()
	is_active = models.BooleanField(default=True)
	
	# This will filter out is_active = False
	objects = BaseManager()
	
	# This will return all rows
	all_objects = models.Manager()
	
	class Meta:
		abstract = True
		
	def save(self, *args, **kwargs):
		"""
		:param args:
		:param kwargs:
		:return: override save method to generate created and modified date
		"""
		if not self.pk:
			self.created_date = datetime.now()
		self.modified_date = datetime.now()
		return super(BaseModel, self).save(*args, **kwargs)
	
	