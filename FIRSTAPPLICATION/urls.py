from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'), #customized url
    #path('page2/',views.index2,name='index2'),
    #path('page3/',views.index3,name='index3'),

]