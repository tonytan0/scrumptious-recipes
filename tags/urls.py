from django.urls import path

from tags.views import (
    show_tags,
    TagCreateView,
    TagUpdateView,
    TagDetailView,
    TagListView,
)

urlpatterns = [
    path("", show_tags, name="tags_list"),
    path("", TagListView.as_view(), name="tag_detail"),
    path("<int:pk>/", TagDetailView.as_view(), names="tag_detail"),
    path("new/", TagCreateView.as_view(), name="tag_new"),
    path("<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
]
