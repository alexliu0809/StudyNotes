from django.shortcuts import render,get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count

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

# The parameters year, month, day, post are parsed in url when you type the url
# Define in urls.py
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


def post_share(request, post_id):

	post = get_object_or_404(Post, id = post_id, status = "published")
	sent = False

	#The view is initially loaded with a post command
	if request.method == 'POST':
		#Create a form using submitted data from post
		form = EmailPostForm(request.POST)
		#valid data in form
		if form.is_valid():
			cd = form.cleaned_data #Return all valid fields as dict
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			#Only by post a email will be sent.
			send_mail(subject, message, 'admin@myblog.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()

	return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})


