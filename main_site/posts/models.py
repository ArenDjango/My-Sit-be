from django.db import models
from django.urls import reverse
from pagedown.widgets import AdminPagedownWidget

# MVC MODEL VIEW CONTROLLER

def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	return "%s/%s" %(instance.id, filename)



class Post(models.Model):
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to=upload_location,
			null=True,
			blank=True,
			width_field="width_field",
			height_field="height_field")

	second_image = models.FileField(upload_to=upload_location,
			null=True,
			blank=True,)

	height_field = models.IntegerField(default=0)

	width_field = models.IntegerField(default=0)

	content = models.TextField()

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	taged = models.CharField(max_length=50, blank=True, null=True, default=None, 
	help_text="Добавьте тег для лучшего поиска") # tags


	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ["-updated"]
