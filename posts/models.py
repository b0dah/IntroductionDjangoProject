from django.db import models

class Meta:
	db_table = 'posts'

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField(default='Text')
	timeStamp = models.DateTimeField(auto_now = True)
	updated = models.DateTimeField(auto_now = True)
	
	id = models.AutoField(primary_key = True)
	post_likes = models.IntegerField(default = 0)
	genre = (
		('r', 'Рассказ'),
		('p', 'Поэма'),
		('rr', 'Рассказ'),
	)
	genre = models.CharField(max_length = 100, verbose_name = 'Жанр', choices = genre,  default = 'r')
	post_author = models.ForeignKey('Author', null = 'True', blank = 'True')
	
	def __unicode__(self):
		return self.title
		
	def __str__(self):
		return self.title


class Author(models.Model):
	id = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	email = models.EmailField
	
	def __unicode__(self):
		return self.first_name + self.last_name
			
	def __str__(self):
		return self.first_name + self.last_name

class Comment(models.Model):
	id = models.AutoField(primary_key = True)
	comment_text = models.TextField(default='...')
	comment_article = models.ForeignKey(Post)
	
	def __unicode__(self):
		return self.comment_text			
	def __str__(self):
		return self.comment_text