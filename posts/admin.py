from django.contrib import admin
from .models import Post
from .models import Author
from .models import Comment

class PostInstanceInline(admin.StackedInline):
	model = Comment
	extra = 2	

class PostModelAdmin(admin.ModelAdmin):
	
	inlines = [PostInstanceInline]
#	fields = ('title',)
	exclude = ('content',)
	ordering = ['-timeStamp']
	
	list_display = ['title', 'content', 'timeStamp', 'updated']
	list_display_links = ['title', 'content', 'timeStamp', 'updated']
	list_filter = ['timeStamp']
#	list_editable = ['title']
	
	class Meta:
		model = Post
		
class AuthorModelAdmin(admin.ModelAdmin):
	list_display = ['first_name']
	ordering = ['last_name', 'first_name']
	
	class Meta:
		model = Author
	
class CommentModelAdmin(admin.ModelAdmin):
	
	class Meta:
		model = Comment

	
# Register your models here.
admin.site.register(Post, PostModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Comment, CommentModelAdmin )





