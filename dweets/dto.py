from django.db import models
from django.forms import model_to_dict


class SerializedResponse(object):
	def __init__(self, success=False, data=None, errors=None, model_class=None):
		self.success = success
		self.data = data
		self.errors = errors
		
	def get_success(self):
		return self.success
	
	def get_data(self):
		if isinstance(self.data, dict):
			return self.data.__dict__
		if hasattr(self.data, 'get_data'):
			return self.data.get_data()
		if isinstance(self.data, models.Model):
			return model_to_dict(self.data)
		return self.data
	
	def get_errors(self):
		return self.errors
