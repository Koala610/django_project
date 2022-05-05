from django.db import models
from message.models import Message

# Create your models here.
class TechCategoryManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(name='tech')



class NatureCategoryManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(name='nature')



class Category(models.Model):
	name = models.TextField(max_length=100, default='', blank=True)
	cover = models.ImageField(default='cover.png', upload_to='covers', blank=True)
	objects = models.Manager()
	techs = TechCategoryManager()
	natures = NatureCategoryManager()


class Post(Message):
	reciever = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='posts')#change on category
	body = models.TextField()
	rating = models.IntegerField(default=0)


