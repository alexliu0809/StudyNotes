from django import forms
from .models import Comment
#create a form
class EmailPostForm(forms.Form):
	#fields in a form
	
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False,widget = forms.Textarea)

#it would be redundant to define the field types in your form
#because you’ve already defined the fields in your model.
#Django provides a helper class that lets you create a Form class from a Django model.
class CommentForm(forms.ModelForm):
	#The generated Form class will have a form field for every model field specified, in the order specified in the fields attribute.
	class Meta:
		model = Comment
		fields = ('name','email','body')
