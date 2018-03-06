from django.urls import path, include


from posts import views

from .views import (
	post_list,
	post_detail,

	)

app_name = 'posts'
urlpatterns = [
  	path('', post_list, name='list'),
    path('<int:id>/', post_detail, name='detail'),
]