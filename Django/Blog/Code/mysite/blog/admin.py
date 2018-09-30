from django.contrib import admin
from .models import Post,Comment

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

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','created','updated','active')
	list_filter = ('active','created','updated')
	search_fields = ('name','email','body')
admin.site.register(Comment,CommentAdmin)