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







