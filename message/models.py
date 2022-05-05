from django.db import models
from users.models import User

# Create your models here.

class Message(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outbox', blank=True)

	class Meta:
		abstract = True