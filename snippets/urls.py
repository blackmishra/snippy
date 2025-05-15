from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

snippet_detail = SnippetViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

snippet_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)

user_list = UserViewSet.as_view({"get": "list"})

user_detail = UserViewSet.as_view({"get": "retrieve"})


urlpatterns = [
    path("", views.api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippet/<int:pk>/", snippet_detail, name="snippet-detail"),
    path(
        "snippet/<int:pk>/highlight",
        snippet_highlight,
        name="snippet-highlight",
    ),
    path("userList/", user_list, name="user-list"),
    path("userDetail/<int:pk>/", user_detail, name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
