from django.urls import path

from .views import ListBlog, ListByCategory, CreateBlog

urlpatterns = [

    path('create/', CreateBlog.as_view()),
    path('listblog/', ListBlog.as_view()),
    path('list/<str:category>/', ListByCategory.as_view())
]
