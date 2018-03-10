from django.db import models
from utils.models import BaseModel


class UserProfile(models.Model):
	# Device Choices
	MOBILE = "mobile"
	DESKTOP = "desktop"
	DEVICE_CHOICES = (
		(MOBILE, MOBILE.title()),
		(DESKTOP, DESKTOP.title()),
	)
	
	user = models.OneToOneField('auth.User', related_name='profile')
	device = models.CharField(max_length=20, choices=DEVICE_CHOICES, default=DESKTOP)
	

class Follower(BaseModel):
	user = models.ForeignKey(UserProfile, auto_created='follower')
	follows = models.ForeignKey(UserProfile, related_name='followed')
	
	def __unicode__(self):
		return self.user.username
	
	



