from django.urls import path

from .views import ListCreateBlog, ListByCategory

urlpatterns = [

    path('create/', ListCreateBlog.as_view()),
    path('list/<str:category>/', ListByCategory.as_view())
]
