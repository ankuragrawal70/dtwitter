from django.db import models
from utils.models import BaseModel
from users.models import UserProfile
from utils.validators import SimpleTweetValidator
from django.forms import model_to_dict


class Dweet(BaseModel):
	"""
	Containing dweet info
	"""
	created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="dweeter")
	content = models.CharField(
		max_length=100, unique=True, validators=[SimpleTweetValidator],
		help_text="Please enter a valid tweet of maximum 100 length character",
		blank=False,
		error_messages={
			'unique': "A dweet with the same content already exists.",
		},)
	
	def get_data(self):
		res = model_to_dict(self)
		res['created_by'] = model_to_dict(self.created_by)
		return res


class Comments(BaseModel):
	"""
	model for all the comments for a particular dweet and by a particular user
	"""
	dweet = models.ForeignKey(Dweet, on_delete=models.CASCADE, related_name="commented_dweet")
	commented_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="commented_by")
	content = models.TextField(blank=False)
	
	def get_data(self):
		res = model_to_dict(self)
		res['dweet'] = model_to_dict(self.dweet)
		res['commented_by'] = model_to_dict(self.commented_by)
		return res


class Likes(BaseModel):
	"""
		model for all the likes for a particular dweet and by a particular user
	"""
	dweet = models.ForeignKey(Dweet, on_delete=models.CASCADE, related_name="liked_dweet")
	liked_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="liked_by")
	
	class Meta:
		unique_together = ('dweet', 'liked_by')
	
	def get_data(self):
		res = model_to_dict(self)
		res['dweet'] = model_to_dict(self.dweet)
		res['liked_by'] = model_to_dict(self.liked_by)
		return res