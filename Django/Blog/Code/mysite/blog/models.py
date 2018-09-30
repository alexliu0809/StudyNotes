from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class PublishManager(models.Manager):
	def get_queryset(self):
		return super(PublishManager, self).get_queryset().filter(status = 'published')

# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length =250)
	slug = models.SlugField(max_length =250, unique_for_date = 'publish')
	author = models.ForeignKey(User, related_name = 'blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')

	objects = models.Manager()
	published = PublishManager() #Define customer manager
	#Only returns published

	#Add tags
	tags = TaggableManager()

	class Meta:
		ordering = ('-publish',) #Sort by publish descending

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#create an url that uses blog:post_detail as display view and pass args to it.
		return reverse('blog:post_detail',args = [
			self.publish.year,
			self.publish.strftime("%m"),
			self.publish.strftime("%d"),
			self.slug
			])

class Comment(models.Model):
	# related_name specifices the name of the reverse relation from Post model back to this model
	# If you dont define the related_name attribute, Django will use comment_set.
	# So potentially you can do Post.comments
	post = models.ForeignKey(Post, related_name = "comments")
	name = models.CharField(max_length = 80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	active = models.BooleanField(default = True)

	class Meta:
		#sort by created
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)


