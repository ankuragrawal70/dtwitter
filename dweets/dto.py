from django.db import models


class SerializedResponse(object):
	def __init__(self, success=False, data=None, errors=None, model_class=None):
		self.success = success
		self.data = data
		self.errors = errors
		self.model_class = model_class or models.Model
	
	def get_success(self):
		return self.success
	
	def get_data(self):
		if self.data:
			if isinstance(self.data, dict):
				return self.data.__dict__
			if isinstance(self.data, self.model_class):
				return self.model_class
		return self.data
	
	def get_errors(self):
		return self.errors
