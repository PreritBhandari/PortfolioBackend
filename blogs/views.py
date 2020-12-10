from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Blog
from .serializers import ListCreateSerializer


# Using Generic Class based views

class ListCreateBlog(ListCreateAPIView):
    serializer_class = ListCreateSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


class ListByCategory(ListAPIView):
    serializer_class = ListCreateSerializer
    lookup_field = 'category'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.kwargs['category']
        return Blog.objects.filter(category=category)
