from django.conf.urls import url
from app1 import views


urlpatterns =[
    url(r'^home/$',views.home),
    url(r'^addbook/$',views.addbook),
]