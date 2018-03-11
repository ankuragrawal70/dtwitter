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
		res['created_by'] = self.created_by.user.email
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
		res['dweet'] = self.dweet.get_data()
		res['commented_by'] = self.commented_by.user.email
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
		res['dweet'] = self.dweet.get_data()
		res['liked_by'] = self.liked_by.user.email
		return res