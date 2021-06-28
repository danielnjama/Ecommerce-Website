from django import forms
from . models import shop,reviews

class reviewForm(forms.ModelForm):
	class Meta:
		model=reviews
		fields=['recommend','review','name','email']
		