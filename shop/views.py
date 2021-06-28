from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from . models import shop,reviews
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User, auth
import smtplib
from email.message import EmailMessage
from newsletter.models import newsletters
from newsletter.forms import NewsletterForm
from . forms import reviewForm
import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import geocoder
from blog.models import *
import requests
from django.db.models import Count



# Create your views here.
def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'index.html')






def register(request):

    if request.method == 'POST':
        first_name= request.POST['name']
        #last_name= request.POST['last_name']
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password1,email=email, first_name=first_name)
                user.save()
                return HttpResponse("Your account has been created. please click login to login")

        else:
            messages.info(request,'password not matching') 
            return redirect('register')       
        return redirect('/')


    else:
        return render(request,'index.html')





def logout(request):
    auth.logout(request)
    return redirect('/')


def desktops(request):
    title = "desktops | CPUs| Monitors | All in one| ex uk desktops"
    allitems = shop.objects.filter(category='desktops')
    return render(request,'product.html',{"allitems":allitems,"title":title})

def laptops(request):
    title = "Laptops |cheap laptops|New laptops ex uk laptops"
    allitems = shop.objects.filter(category='laptops')
    return render(request,'product.html',{"allitems":allitems,"title":title})

def accessories(request):
    title = "Laptop accessories | desktop accessories | computer accessories"
    allitems = shop.objects.filter(category='accessories')
    return render(request,'product.html',{"allitems":allitems,"title":title})

def index(request):
    title = "Laptops | Desktops | accessories | new and refurbished"
    allitems = shop.objects.all()
    return render(request,'index.html',{'allitems':allitems,"title":title})


def contacts(request):
    if request.method =="POST":
        name = request.POST.get('name')
        from_email = request.POST.get('email',)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message = 'Name: {} \nEmail: {}\n{}'.format(name,from_email,message)
        recipient = settings.EMAIL_HOST_USER
        if subject != "" and message != "" and from_email != recipient:
            send_mail(subject=subject,message=message,from_email=from_email ,recipient_list=[recipient,],fail_silently=False)
            #emailing=EmailMessage(subject=subject,body=message,from_email=request.POST.get('email',) ,to=[recipient,])
            #emailing.send()
            message='Your message has been sent. Thank you for choosing Dynamic Technologies\nYour only trusted IT partner'
        else:
            message = "your email has not been sent. Kindly check that all the fields are correct"
        return render(request,'message.html',{'message':message})
    return render(request,'contact.html')


def search(request):
    search = request.GET.get('q')
    allitems = shop.objects.filter(name__contains=search)
    return render(request,'search.html',{'allitems':allitems})



def item_detail(request,slug,category):
    item = get_object_or_404(shop,slug=slug)
    category=item.category
    #count_views = shop.objects.get(item.id)
    item.shopviews +=1
    item.save()
    related_searches = shop.objects.filter(category =item.category).exclude(id=item.id)
    if request.method == 'POST':
        form = reviewForm(request.POST)
        if form.is_valid():
            validform = form.save(commit=False)
            validform.shops = item
            validform.date =datetime.datetime.now().strftime('%Y-%m-%d')
            validform.save()

    return render(request,'single.html',{'item':item,'related_searches':related_searches})


def newsletter(request):
    	if request.method =='POST':
            newsform = NewsletterForm(request.POST)
            if newsform.is_valid:
                cleanForm=newsform.save(commit=False)
                if newsletters.objects.filter(email=cleanForm.email).exists():
                    message ='you are alredy subscribed to our news letters'
                    return render(request,'message.html',{'message':message})
                else:
                    cleanForm.save()
                    message ='you have successfully subscribed to our news letter.\nStay tunned for future updates'
                    subject = 'Welcome to Dynamic TechNologies Newsletter'
                    from_email = 'client@dtechnologies.co.ke'
                    to_email = cleanForm.email
                    #send_mail(subject,message,from_email,[to_email])
                    html_message = render_to_string('newsletter_subscription.html', {'message': message})
                    plain_message = strip_tags(html_message)
                    mail.send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)      
                    return render(request,'message.html',{'message':message})


def about(request):
    return render(request,'about.html',{})

@user_passes_test(lambda u: u.is_superuser)
def send_newsletter(request):
    subscribers = newsletters.objects.all()
    emails = []
    for i in subscribers:
        emails.append(i.email)
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        from_email = settings.EMAIL_HOST_USER
        
        """ if subject !="" and message !="" and from_email != "" and len(emails) !=0:
            try:
                send_mail(subject,message,from_email,emails)
            except:
                return HttpResponse("An error occured and we couldn't send your message!Please try again later")
        else:
            return HttpResponse("An error occured and we couldn't send your message!Please try again later") """
        html_message = render_to_string('newsletter_subscription.html', {'message': message})
        plain_message = strip_tags(html_message)
        mail.send_mail(subject, plain_message, from_email, emails, html_message=html_message)

        
        
    return render(request,'newsletter.html',{"subscribers":subscribers})


def unsubscribe(request):
    message =""
    if request.method == "POST":
        email = request.POST.get("email")
        unsubscribe_email = newsletters.objects.filter(email=email)
        if len(unsubscribe_email) !=0:
            unsubscribe_email.delete()
            message = "you have successfully been unsubscribed from our mailing list. Should you by any chance wish to come back, please register your email again in the subscribe to news letter section"
        else:
            message = "This email does not exist in our mailing list"

    return render(request,"unsubscribe.html",{"message":message})




def blogs(request):
    blogs =blogpost.objects.filter(publish=True)
    ads = shop.objects.order_by("?").first()
    return render(request,'blog.html',{"blogs":blogs,"ads":ads})

def social(request):
    blogs =blogpost.objects.filter(tags='social')
    ads = shop.objects.order_by("?").first()
    return render(request,'blog.html',{"blogs":blogs,"ads":ads})

def technology(request):
    blogs =blogpost.objects.filter(tags='technology')
    ads = shop.objects.order_by("?").first()
    return render(request,'blog.html',{"blogs":blogs,"ads":ads})

def political(request):
    blogs =blogpost.objects.filter(tags='political')
    ads = shop.objects.order_by("?").first()
    return render(request,'blog.html',{"blogs":blogs,"ads":ads})


def blog_detail(request,slug):
    blogs = get_object_or_404(blogpost,slug=slug)
    popblogs =blogpost.objects.filter(publish=True)
    viewers = cviews.objects.all()
    blogposts =blogpost.objects.filter(publish=True)
    #y=cviews.objects.values("post").annotate(Count("post"))
    if request.method == "GET":
        r = requests.get('https://api.ipdata.co?api-key=test').json()
        save_instance = cviews(post=blogs,count=1,location=r['country_name'])
        save_instance.save()
    
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        commentpost = request.POST.get("message")

        comment_save = comments(post=blogs,name=name,email=email,commentpost=commentpost)
        comment_save.save()
            
    return render(request,'single-blog.html',{'blogs':blogs,'popblogs':popblogs})


def search_blog(request):
    search = request.GET.get('q')
    blogs = blogpost.objects.filter(title__contains=search)
    return render(request,'blog.html',{"blogs":blogs})