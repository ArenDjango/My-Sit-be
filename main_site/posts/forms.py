from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"second_image",
			"taged",
		]