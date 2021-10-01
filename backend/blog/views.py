from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Blog
from blog.serializer import BlogSerializer

class BlogListView(ListAPIView):
    queryset = Blog.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogFeaturedView(ListAPIView):
    queryset = Blog.objects.all().filter(featured=True)
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogCategoryView(APIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get_object(self, category):
        try:
            return Blog.objects.order_by('-date_created').filter(category__iexact=category)
        except Blog.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, category):
        queryset = self.get_object(category)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
