from django.urls import path

from .views import BlogListView, BlogCreateView, BlogDetailView , BlogUpdateView, BlogDeleteView, BlogProfileListView


urlpatterns = [
   path("post/new/", BlogCreateView.as_view(), name="new_post"),
   path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
   path('', BlogListView.as_view(), name='home'),
   path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
   path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
   path("post/<int:pk>/profile/", BlogProfileListView.as_view(), name="profile"),
]