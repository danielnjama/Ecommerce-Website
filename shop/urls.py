from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index,name='index'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$',views.item_detail,name='item_detail'),
    path('contacts/',views.contacts,name='contacts'),
    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path('subscribe-newsletter/',views.newsletter,name='newsletter'),
    path('send-newsletter/',views.send_newsletter,name='send_newsletter'),
    path("about-us/",views.about,name="about"),
    path('search',views.search,name ='search'),
    path('desktops/',views.desktops,name ='desktops'),
    path('laptops/',views.laptops,name ='laptops'),
    path('accessories/',views.accessories,name ='accessories'),
    path("unsubscribe/",views.unsubscribe,name="unsubscribe"),
    path("social/",views.social,name="social"),
    path("political/",views.political,name="political"),
    path("technology/",views.technology,name="technology"),
    path("search-blog/",views.search_blog,name="search_blog"),
    path("blog/",views.blogs,name="blogs"),
    url(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name='blog_detail'),
   

    
    
] 



