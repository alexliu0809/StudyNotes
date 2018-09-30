# Building A Blog
## Install Django
```shell
python -m pip install django==1.11.7

django-admin.py startproject wisdompets
```

## Start A Project
```shell
django-admin.py startproject blog
```

## Migrate
```shell
python manage.py migrate
```

## Run with nothing
```shell
python manage.py runserver 127:0:0:1:8001
```

## Deploy
See: docs.djangoproject.com/howto/deployment/wsgl

## Project / Applications
* The term project describes a Django web application. The project Python package is defined primarily by a settings module, but it usually contains other things. For example, when you run django-admin startproject mysite you’ll get a mysite project directory that contains a mysite Python package with settings.py, urls.py, and wsgi.py. The project package is often extended to include things like fixtures, CSS, and templates which aren’t tied to a particular application.

A project’s root directory (the one that contains manage.py) is usually the container for all of a project’s applications which aren’t installed separately.

The term application describes a Python package that provides some set of features. Applications may be reused in various projects.

Applications include some combination of models, views, templates, template tags, static files, URLs, middleware, etc. They’re generally wired into projects with the INSTALLED_APPS setting and optionally with other mechanisms such as URLconfs, the MIDDLEWARE setting, or template inheritance.

## Create Data Model
* Add code to models.py
* Register app in settings.py
* migrate


## Create Administartion Site
Goals here:
* Create Admin Site

```shell
python manage.py createsuperuser
```

Then you can log in to localhost/admin by using the super username and pw.

### Register Models
Register Models in admin so that models can be edited through admin site.
```python
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

	#Define how to display the model data when queried.
	list_display = ('title','slug','author','publish','status')
	list_filter = ('status','created','publish','author')
	search_fields = ('title','body')
	prepoulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierachy = 'publish'
	ordering = ['status','publish']

#admin.site.register(Post)
#PostAdmin describes how it is displayed in admin site
admin.site.register(Post,PostAdmin) 
```

## Working with QuerySet and Managers
Manager: manages models. Basically doing query here. Can also be managed through admin set. 

Goals Here:
* Create, update, retrieve objects
* Create model manager.

```shell
python manage.py shell
```

```python
from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username='admin')
post = Post.objects.create(title = "xxx", slug='xxx', body = 'xxx', author = user)
post.save()
post.title = "New Title"
all_posts = Post.objects.all()
```

### Customize Model Managers
Objests are the default model manage. Define customer. 

Add to model.py
```python
class PublishManager(models.Manager):
	#Specify return type

	def get_queryset(self):
		return super(PublishManager, self).get_queryset().filter(status = 'published')


class model_name:
	published = PublishManager() #Define customer manager
	#Only returns published
```
Then you return python, and 
```python
Post.published.filter
```
## Building List and Detail Views.
* Create application views and define URL pattern for each view.
* Add URL pattern for views

### Create Views
* Add code to view.py
```python
def post_list(request):
	#created a view to display list of posts.
	posts = Post.published.all()

	#First para: request, 
	#Second para: which template in to use (template path (the path in templates))
	#Third para: parameter to pass to template as input
	return render(request, 'blog/post/list.html', {'posts':posts})

# The parameters year, month, day, post are parsed in url when you type the url
# Define in urls.py
def post_detail(request, year, month, day, post):
	#created a view to display a single post
	post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)
	return render(request, 'blog/post/detail.html',{'post',post})
```

### Add url patterns
Django runs through each url pattern and stops at the first match. Then Django imports the view that matches the URL and returns.

Create urls.py in blog directory, add:
```python
from django.conf.urls import url
from . import views

urlpatterns = [

	# Navigate to post_list if no para
	# First para: url pattern
	# Second para: the view to open, the view is defined in views.py
	# name the url
    url(r'^$', views.post_list, name = 'post_list'),

    # Navigate to detail if year+month+day+postinfo
    # Name of this url is 'post_detail'
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    views.post_detail,
    name = 'post_detail')
]
```

Register these urls in project
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Give a name space to this block of urls. (defined in blog/urls)
    url(r'^blog/',include('blog.urls',namespace='blog',app_name='blog')),
]
```

### Reverse Function
Something similar to the url template tag in your code. (create a formatted url)

Add following to models.py so that it auto creates an url that uses blog:post_detail template. 
```python
def get_absolute_url(self):
		#create an url that uses blog:post_detail as display view and pass args to it.
		return reverse('blog:post_detail',args = [
			self.publish.year,
			self.publish.strftime("%m"),
			self.publish.strftime("%d"),
			self.slug
			])
```

## Create Templates For Views
* Add templates to display posts
* Build file structure for templates

Create the following file structure:
```bash
blog/
├── templates/
	├── blog/
		├── base.html
		├── post/
			├── detail.html
			├── list.html
```
base.html contains the frame for detail and list. While detail and list only implements the content part. See base.html for more detail. Also list and list will have a parameter of object, where they can use them to generate content.

### Place CSS File
To read CSS file correctly, add to settings.py:
```python 
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```
Also place static directory under mysite, so it books like:
```bash
mysite/
├── blog/
├── mysite/
├── static/
```

## Creating And Handle Forms
How to Create forms and handle forms in views. Also send it if possible
### Create form.py, add:
```python
#create a form
class EmailPostForm(forms.Form):
	#fields in a form
	
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget = forms.Textarea)

```
This defines a Form class. A Form instance has an is_valid() method, which runs validation routines for all its fields. 

The whole form, when rendered for the first time, will look like:
```html
<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required />
```

### Create a view that contains this form. 
Form data sent back to a Django website is processed by a view, generally the same view which published the form. 

To handle the form we need to instantiate it in the view for the URL where we want it to be published:

Add this to views.py:
```python
#Also register this view in urls.py so that this view will be called when a specific url is typed.
#url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share')

def post_share(request, post_id):

	post = get_object_or_404(Post, id = post_id, status = "published")
	sent = False

	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = EmailPostForm(request.POST)
		#valid data in form
		if form.is_valid():
			cd = form.cleaned_data #Return all valid fields as dict
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'admin@myblog.com', [cd['to']])
			sent = True
	else: # if a GET (or any other method) we'll create a blank form
		form = EmailPostForm()

	return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})

```
If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = Form(request.POST) This is called “binding data to the form” (it is now a bound form).

We call the form’s is_valid() method; if it’s not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute. We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.

### Create Corresponding template
Add to detail.html so that there's a link to share page:
```html
<p><a href="{% url 'blog:post_share' post.id %}">Share This Post</a></p>
```
Add share.html:
```html
<form action="." method="post">
    {{ form.as_p }} <!--render form as paragraph, as_ul, as_table -->
    {% csrf_token %} <!--hidden field void attacks-->
    <input type="submit" value="Send e-mail"> <!-- add submit -->
</form>
```

### Add Email Settings:
Notice that only way to send an email is to set from email same as below. Also, the way this works is that first time it is displayed as get method. So an empty form is created. When you hit submit, it will reload the page using post method. See python code that if post method, an email will be sent, and it will be verified against what's below.

In setting.py, add:
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'fdsfa@gmail.com'
EMAIL_HOST_PASSWORD = 'cxvzwef'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Create Comment System
### Create A Model That Saves the comments
Add to model.py and migrate.
```python
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
```
### Add a form so that comments can be submitted through forms.
Add to forms.py
```python
#it would be redundant to define the field types in your form
#because you’ve already defined the fields in your model.
#Django provides a helper class that lets you create a Form class from a Django model.
class CommentForm(forms.ModelForm):
	#The generated Form class will have a form field for every model field specified, in the order specified in the fields attribute.
	class Meta:
		model = Comment
		fields = ('name','email','body')
```

### Modify Corresponding Post Views
Change post_detail
```python
def post_detail(request, year, month, day, post):
	#created a view to display a single post
	post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)

	comments = post.comments.filter(active = True)

	is_new_comment = False

	if request.method == 'POST':

		comment_form = CommentForm(request.POST)

		if comment_form.is_valid():

			#Dont save now
			new_comment = comment_form.save(commit=False)

			new_comment.post = post

			new_comment.save()

			is_new_comment = True
	else:

		comment_form = CommentForm()

	return render(request, 'blog/post/detail.html',{'post':post,'comments':comments,'comment_form': comment_form,'new_comment':is_new_comment})
```

### Update Detail.html
Append to detail.html:
```html
{% with comments.count as total_comments%}
	<h2>
		{{total_comments}} comment{{total_comments|pluralize}}
	</h2>
{% endwith%}

{% for comment in comments %}
<div class="comment">
	<p class="info">
	Comment {{forloop.counter}} by {{comment.name}} {{comment.created}}
	{{comment.body|linebreaks}}
	</p>
</div>
{% empty %}
<p>No Comments Yet</p>
{% endfor %}

{% if new_comment %}
<h2> Your comment has been added </h2>
{% else %}
<h2>Add a comment</h2>
<form action="." method="post">
	{{comment_form.as_p}}
	{%csrf_token%}
	<p><input type="submit" value="Add Comment"></p>
</form>
{%endif%}
```

## Add Tagging Functionality
### Install tagging from pip
```shell
python3 -m pip install django-taggit==0.17.1
```
### Add taggit to installed_apps in settings.py.
```python
INSTALLED_APPS = [
    'blog',
    'taggit',
]
```
### Add taggit to models so that posts can be tagged
In model.py, add and migrate:
```python
from taggit.managers import TaggableManager
class Post(models.Model):
	### blahblah ###
	objects = models.Manager()
	published = PublishManager() #Define customer manager
	#Only returns published

	#Add tags
	tags = TaggableManager()
```
When you installed taggit and use TaggableManager in any model, it will be added to admin web automatically (a place for tag, also Post will also have tags).

### Modify List.html and show the tags
```html
<p class="tags">
		Tags:
		{{post.tags.all|join:", "}}
</p>
```

### Use Pagination While displaying Posts.
Pagination: Django provides a few classes that help you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links. These classes live in django/core/paginator.py.

#### Change Views.py
```python
from taggit.models import Tag
# Create your views here.
def post_list(request, tag_slug = None):
	#created a view to display list of posts.
	object_list = Post.published.all()
	tag=None

	if tag_slug:
		#get the corresponding tag that's related to tag_slug
		tag = get_object_or_404(Tag,slug = tag_slug)
		#Get all objects with the tag (not tag_slug)
		object_list = object_list.filter(tags__in=[tag])

	paginator = Paginator(object_list, 3) #3 posts each page
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	#First para: request, 
	#Second para: which template in to use (template path (the path in templates))
	#Third para: parameter to pass to template as input
	return render(request, 'blog/post/list.html', {'posts':posts,'page':page, 'tag':tag})
```

#### Add pagination to list.html
Add pagination.html to templates
```bash
templates/
├── blog/
├── pagination.html/
```
Here's how it looks like:
```html
<div class="pagination">
    <span class="step-links">
        {% if page.has_previous %}
            <a href="?page={{ page.previous_page_number }}">Previous</a>
        {% endif %}

        <span class="current">
            Page {{ page.number }} of {{ page.paginator.num_pages }}.
        </span>

        {% if page.has_next %}
            <a href="?page={{ page.next_page_number }}">Next</a>
        {% endif %}
    </span>
</div>
```

Include pagination part to list.html at the end
```html
{% include "pagination.html" with page=posts %}
```

### Enabling Searching For Posts With Specific Tags
post_list is ready for searching for specific tags, as an optional para is defined.
#### Register URL to search for posts with specific tag. 
```python
#Add this so that a tag will be searched
# First pattern doesn't pass para
url(r'^$', views.post_list, name = 'post_list'),
# Second gives one para
url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list,name='post_list_by_tag'),
```
#### Change Tags' display in list.html so that can be clicked
```html
<!-- New Tag Display -->
Tags:
		{%for tag in post.tags.all%}
			<a href="{% url 'blog:post_list_by_tag' tag.slug %}">{{tag.name}}</a>
			{% if not forloop.last%}
			,
			{%endif%}
		{%endfor%}
```

## Retrieving Post By Similarity
Find posts sharing many tags. 
### Add code detail.view
```python
from django.db.models import Count

# List of similar posts

# Retrieve a list of ids for tags of current post. 
# flag list like [1,2,3]
post_tags_ids = post.tags.values_list('id', flat=True)
print(post_tags_ids)
#exclude the current post from all
similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
#Count same tags and order and get first 4.
similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:1]
print(similar_posts)

return render(request, 'blog/post/detail.html',{'post':post,'comments':comments,'comment_form': comment_form,'new_comment':is_new_comment,'similar_posts':similar_posts})
```
### Edit detail.html so that similars are displayed
```python
<h2>Similar posts</h2>
{% for post in similar_posts %}
<p><a href="{{ post.get_absolute_url }}">{{post.title}}</a></p>
{% empty %}
There are no similar posts yet.
{% endfor%}
```

## Creating Customer Template Tags / Filters
See this [link](https://docs.djangoproject.com/en/1.7/topics/templates/) for more info. 
#### Templates
A template is simply a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

Below is a minimal template that illustrates a few basics.
```html
{% for story in story_list %}
{% block content %}
<h1>{{ section.title }}</h1>
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
```
#### Variables
Variables look like this: {{ variable }}. When the template engine encounters a variable, it evaluates that variable and replaces it with the result. Variable names consist of any combination of alphanumeric characters and the underscore ("_"). Use a dot (.) to access attributes of a variable.

#### Filters
You can modify variables for display by using filters.

Filters look like this: {{ name|lower }}. This displays the value of the {{ name }} variable after being filtered through the lower filter, which converts text to lowercase. Use a pipe (|) to apply a filter.

Filters can be “chained.” The output of one filter is applied to the next. {{ text|escape|linebreaks }} is a common idiom for escaping text contents, then converting line breaks to <p> tags. 

Some filters take arguments. A filter argument looks like this: {{ bio|truncatewords:30 }}. This will display the first 30 words of the bio variable.

Filter arguments that contain spaces must be quoted; for example, to join a list with commas and spaced you’d use {{ list|join:", " }}.

#### Tags
Tags look like this: {% tag %}. Tags are more complex than variables: Some create text in the output, some control flow by performing loops or logic, and some load external information into the template to be used by later variables.

### Create template tags
See this [link](https://docs.djangoproject.com/en/1.7/topics/templates/) for more info.

The app should contain a templatetags directory, at the same level as models.py, views.py, etc. If this doesn’t already exist, create it - don’t forget the __init__.py file to ensure the directory is treated as a Python package. 

Your custom tags and filters will live in a module inside the templatetags directory. The name of the module file is the name you’ll use to load the tags later, so be careful to pick a name that won’t clash with custom tags and filters in another app.

#### Create A Folder and Files.
```shell
mysite/
├── blog/
	├── templates/
	├── admin.py
	├── templatetags/
		├── blog_tags.py/ #Use name of this file to load tags
```

#### Add Code to Blog_tags
```python
from django import template
 
#To be a valid tag library, the module must contain a module-level variable named register that is a template.Library instance, in which all the tags and filters are registered.
register = template.Library()

from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# Process any data and add it to any template regardless of the view executed.
# Like global variable

#Many template tags take a number of arguments – strings or template variables – and return a result after doing some processing based solely on the input arguments and some external information. 
#To ease the creation of these types of tags, Django provides a helper function, simple_tag. This function, which is a method of django.template.Library, takes a function that accepts any number of arguments, wraps it in a render function and the other necessary bits mentioned above and registers it with the template system.
#This example, simple tag takes no args and return count.
@register.simple_tag
def total_posts():
	return Post.published.count()

#Another common type of template tag is the type that displays some data by rendering another template.
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count = 2):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts':latest_posts}

#Processes the data and sets a variable in the context
#Assignment tags are like simple tags but they store the result in a given variable.
@register.assignment_tag
def get_most_commented_posts(count = 2):
	return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name="markdown")
def markdown_format(text):
	return mark_safe(markdown.markdown(text))
```

#### Edit Corresponding HTML
The tags are used as function name. 

For simple_tag, edit base.html
```html
{% load blog_tags %}
<p>This is my blog. I've Written {% total_posts %} posts so far</p>
```
For inclusion_tag, create latest_posts.html
```html
<ul>
{% for post in latest_posts %}
	<li>
		<a href="{{post.get_absolute_url }}">{{post.title}}</a>
	</li>
{% endfor %}
</ul>
``` 

Edit base.html
```html
<h2>
	My blog
</h2>
<p>
	This is my blog. I've Written {% total_posts %} posts so far
</p>
<h3>
	Latest Posts
</h3>
{% show_latest_posts %}
```

For assignment_tag, edit base.html
```html
<h3>
	Most commented posts
</h3>
	{% get_most_commented_posts as most_commented_posts %}
<ul>
	{% for post in most_commented_posts %}
	    <li><a href="{{post.get_absolute_url}}">{{post.title}}</a></li>
	{% endfor %}
</ul>
```


### Create Template Filters
See this [link](https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/) for more info.

Install markdown for python, so that text can be displayed as markdown. Add the following code to blog_tags.py:
```python
import markdown

#The Library.filter() method takes two arguments:
#The name of the filter – a string.
#The compilation function – a Python function (not the name of the function as a string)
@register.filter(name="markdown")
def markdown_format(text):
	return mark_safe(markdown.markdown(text))

#If Your filter does not introduce any HTML-unsafe characters (<, >, ', " or &) into the result that were not already present. 
#In this case, you can let Django take care of all the auto-escaping handling for you. 
#All you need to do is set the is_safe flag to True

#Alternatively, your filter code can manually take care of any necessary escaping. 
#This is necessary when you’re introducing new HTML markup into the result.
#ou want to mark the output as safe from further escaping so that your HTML markup isn’t escaped further, 
#so you’ll need to handle the input yourself.
#To mark the output as a safe string, use django.utils.safestring.mark_safe().
#markdown returns html
```

Edit list.html
```html
{% load blog_tags %}
{{post.body|markdown|truncatewords_html:30}}
```

detail.html
```html
{% load blog_tags %}

{% for comment in comments %}
	<div class="comment">
		<p class="info">
		Comment {{forloop.counter}} by {{comment.name}} {{comment.created}}
		{{comment.body|markdown}}
		</p>
	</div>
{% empty %}
<p>No Comments Yet</p>
{% endfor %}
```

## Adding SiteMap
See this [link](https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/) for more.

What are Sitemaps?

Sitemaps are an easy way for webmasters to inform search engines about pages on their sites that are available for crawling. In its simplest form, a Sitemap is an XML file that lists URLs for a site along with additional metadata about each URL (when it was last updated, how often it usually changes, and how important it is, relative to other URLs in the site) so that search engines can more intelligently crawl the site.

The Django sitemap framework automates the creation of this XML file by letting you express this information in Python code.

What is site framework in Django?

Here is an example. In Devsar, we develop “Find Your Trainer”, an online platform to book personal trainers in many states of the USA (another post in this blog explains this project in more detail). And at the moment, FYT organization is being associated with another fitness app, “Your Trainer”.

This is the situation: both sites have trainer objects. Some trainers have to appear either on one site or the other, while some should be on both.

Django comes with a “sites” framework which helps you to manage this. It lets you associate objects and functionality to particular websites. You can have separated software with independent data, but maybe it’s useful to use that data together. The framework is based on a simple “Site” model which stores the domain and name of a website.

### Install "sites" and "sitemap" frame work
Add to setting.py and Migrate.
```python
SITE_ID = 1

INSTALLED_APPS = [

    'django.contrib.sites',
    'django.contrib.sitemaps'
]
```

### Add sitemaps.py under blog/ directory
```python
from django.contrib.sitemaps import Sitemap
from .models import Post

# Let’s assume you have a blog system, with an Post model, 
# and you want your sitemap to include all the links to your individual post entries.
# Here’s how your sitemap class might look:

class PostSitemap(Sitemap):
	#changefreq and priority are class attributes corresponding to <changefreq> and <priority> elements, respectively.
	changefreq = 'weekly'
	priority = 0.9

	#items() is simply a method that returns a list of objects. The objects returned will get passed to any callable methods corresponding to a sitemap property (location, lastmod, changefreq, and priority).
	def items(self):
		return Post.published.all()

	#lastmod should return a datetime.
	def lastmod(self,obj):
		return obj.publish
```

### Add sitemap url to urls.py under mysite/
mysite/urls.py
```python
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
```

You can then visit:
* http://127.0.0.1:8000/admin/sites/site/
* http://127.0.0.1:8000/sitemap.xml

## Search Engine
Use Solr with Django to build a search engine for the blog.

See this [link](https://www.lynda.com/Django-tutorials/Django-1-Building-Blog) for more.






























