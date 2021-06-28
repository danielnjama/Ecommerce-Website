from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
#from multiselectfield import MultiSelectField





#tags=MultiSelectField(choices=cat,max_choices=3,max_length=3)
# Create your models here.


class tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
    


class blogpost(models.Model):
    cat=(
    ("technology",'technology'),
    ("social",'social'),
    ("political",'political'),
)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    tags = models.CharField(choices=cat,max_length=120)
    body = RichTextField()
    slug = models.SlugField(unique=True,max_length=150)
    image = models.ImageField(upload_to='blogimages',blank=True,null=True,help_text="width:555px by height:280px")
    publish = models.BooleanField(default=False)
    datepost = models.DateTimeField(default=datetime.now, blank=True)
    tag = models.ManyToManyField('tags')

    def clean(self):
        if self.image:
            w,h = get_image_dimensions(self.image)
            if w <= 554 and h <= 279:
                raise ValidationError("The image dimensions expected is atlest width 555px and atlest height 280px")
            else:
                return self.image

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-datepost']
    
    

class comments(models.Model):
    post=  models.ForeignKey(blogpost,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    commentpost = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    publish =models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

class cviews(models.Model):
    post = models.ForeignKey(blogpost,on_delete=models.CASCADE)
    location = models.CharField(max_length=150,blank=True)
    date = models.DateTimeField(default=datetime.now())
    count = models.IntegerField(default=0)

    