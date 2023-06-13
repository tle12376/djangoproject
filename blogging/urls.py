from django.urls import path
from blogging.views import stub_view, BlogDetailView, BlogListView

urlpatterns = [
    # path("", stub_view, name="blog_index"),
    # path("posts/<int:post_id>/", stub_view, name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
