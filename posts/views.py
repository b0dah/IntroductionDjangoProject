from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import context

from .models import Post, Author, Comment
from .forms import PostForm

def post_home(request):
	home = 'that is a home page'
	return render_to_response('home.html', {'name':home} )
# Create your views here.

def post_detail(request, id=None):
	instance = get_object_or_404(Post,id=id)
	context = {'title':'Post Detail', 'instance': instance}
	return render(request, 'post_detail.html', context)
	
def post_update(request, id = None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance = instance)
	
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		
	context = {
			'pageFunction': 'Update', 
			'title': instance.title,
			'instance': instance,
			'form': form
		}
	return render(request, 'post_create.html', context)

def post_delete(request):
	return HttpResponse('<h4> ma header </h4>')
	
def post_create(request):
#	form=PostForm()
#	if request.method == 'POST':
#		title = request.POST.get('title')
#		content = request.POST.get('content')
#		Post.objects.create(title=title, content = content) 
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	
	context = {
		'pageFunction': 'Create', 
		'form':form
	}

	return render(request, 'post_create.html', context)
	
def post_list(request):
	queryset = Post.objects.all()
	context = {'queryset':queryset, 'title': 'Posts List'}
	return render(request, 'index.html', context)