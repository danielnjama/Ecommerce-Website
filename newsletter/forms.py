from django import forms
from . models import newsletters

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = newsletters
		fields = ('email',)