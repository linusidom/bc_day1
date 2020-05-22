from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class BillingProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

def post_save_user_created(sender, instance, created, *args, **kwargs):
	if created and instance.email:
		BillingProfile.objects.create(user=instance, email=instance.email)

post_save.connect(post_save_user_created, sender=User)