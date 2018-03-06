from django.contrib import admin

from .models import *

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated"]
	list_display_links = ["updated"]
	list_filter = ["updated"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)