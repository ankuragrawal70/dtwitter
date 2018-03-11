from django.db import models
from datetime import datetime
from django.utils import timezone
from utils.managers import BaseManager


class BaseModel(models.Model):
	"""
	Abstract Base model containing timestamp and active status fields.
	This model can be inherited in every other model to reuse
	the time stamp and active status
	"""
	created_date = models.DateTimeField(default=timezone.now(), editable=False)
	modified_date = models.DateTimeField(blank=True)
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
		if not self.pk and not self.created_date:
			self.created_date = timezone.now()
		self.modified_date = timezone.now()
		return super(BaseModel, self).save(*args, **kwargs)
	
	