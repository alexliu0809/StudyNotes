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