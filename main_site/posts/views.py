from django.utils.six.moves.urllib.parse import (
    quote, quote_plus, unquote, unquote_plus, urlencode as original_urlencode,
)
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

#Pagination import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

from pagedown.widgets import AdminPagedownWidget




# Когда заходиш Post.objects.get
def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(instance.content)
	context = {
		"title": "Detail",
		"instance": instance, 
		"share_string": share_string,
		
	}
	return render(request, 'post_detail.html', context)



# До входа Post.objects.get
def post_list(request):
	queryset_list = Post.objects.all()#.order_by("-updated")


	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)| 
			Q(taged=query))
	""" !!!
	 если title то точное имя если с __icontains то совпадение
	__icontains не переменная это функция 
	"""


	
	"""
	# django filter in tags
	djdj = request.GET.get("djangoname")# значение из ссылки django
	if djdj:
		queryset_list = queryset_list.filter(
			Q(taged=djdj)

			)
	"""
	



	paginator = Paginator(queryset_list, 4) # Max 4 Articles
	page_request_var = "page"

	page = request.GET.get(page_request_var)
	queryset = paginator.get_page(page)
	
	context = {
		"object_list": queryset, 
		"title": "list",
		"page_request_var": page_request_var
	}
	return render(request, 'post_list.html', context)













