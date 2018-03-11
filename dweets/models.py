from django.db import models
from utils.models import BaseModel
from users.models import UserProfile
from utils.validators import SimpleTweetValidator


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


class Comments(BaseModel):
	"""
	model for all the comments for a particular dweet and by a particular user
	"""
	dweet = models.ForeignKey(Dweet, on_delete=models.CASCADE, related_name="commented_dweet")
	created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="commented_by")
	content = models.TextField(blank=False)
	

class Likes(BaseModel):
	"""
		model for all the likes for a particular dweet and by a particular user
	"""
	dweet = models.ForeignKey(Dweet, on_delete=models.CASCADE, related_name="liked_dweet")
	created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="liked_by")
	

