from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError



# Create your models here.
#auto_now_add=True


groups = [
	('laptops','laptops'),
    ('desktops','desktops'),
	('accessories','accessories'),
    ('others','others'),
	
]

state =[
    ('New','New'),
    ('Ex uk','Ex uk'),
]

class shop(models.Model):
    image1 =models.ImageField(upload_to='image51862926581',help_text="width >=255px,heigth >=291px")
    image2 =models.ImageField(upload_to='image51862926581',help_text="width >=255px,heigth >=291px: this field can be blank",blank=True,null=True)
    name = models.CharField(max_length=150)
    condition = models.CharField(max_length=100,choices=state,default="New")
    category = models.CharField(max_length=120, choices= groups)
    description = models.TextField()
    slug = models.SlugField(max_length=150,unique=True)
    price = models.IntegerField()
    instock = models.BooleanField(default=True)
    pricebefore = models.IntegerField(default=0)
    datepost = models.DateTimeField(default=datetime.now, blank=True)
    shopviews = models.IntegerField(default=0)


    def clean(self):
        if not self.image1:
            raise ValidationError("No image selected!")
        else:
            w,h = get_image_dimensions(self.image1)
            if w <= 254 and h <= 290:
                raise ValidationError("The image dimensions expected is atlest width 255px and atlest height 291px")
            else:
                return self.image1





    class Meta:
        ordering = ['-datepost']

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        kwargs = {
            'category': self.category,
            'slug': self.slug
        }
        return reverse('item_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = (self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class reviews(models.Model):
    shops=  models.ForeignKey(shop,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,default="admin@gmail.com")
    recommend = models.CharField(max_length=50)
    review = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
