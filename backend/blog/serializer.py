from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        lookup_field = 'slug' # model field that should be used for
        # performing object lookup of individual model instance. default to 'PK'
        # ngganti primary key di URL, menyesuaikan bussines case.