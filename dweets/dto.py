class SerializedResponse(object):
	def __init__(self, success=False, data=None, errors=None):
		self.success = success
		self.data = data
		self.errors = errors
	
	def get_success(self):
		return self.success
	
	def get_data(self):
		return self.data
	
	def get_errors(self):
		return self.errors
