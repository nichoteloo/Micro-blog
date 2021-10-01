from django.urls import path
from .views import BlogListView, BlogDetailView, BlogFeaturedView, BlogCategoryView

urlpatterns = [
    ## from top to down sequens, please give attention to the order
    path('', BlogListView.as_view()),
    path('featured', BlogFeaturedView.as_view()),
    path('category/<category>', BlogCategoryView.as_view()),
    path('<slug>', BlogDetailView.as_view()),
]