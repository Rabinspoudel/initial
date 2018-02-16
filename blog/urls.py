from django.conf.urls import url
from blog.views import index,home,about,contact,get_one_post


urlpatterns=[
    url(r'^$',index),
    url(r'home/',home),
    url(r'post/(?P<pk>\d+)',get_one_post,name = "detail"),
    # ?p parameter ho python le deko..... \d bhaneko digit recognize hanne ho regular expression ma pk bhaneko primary key
    url(r'about/',about),
    url(r'contact/',contact),

]