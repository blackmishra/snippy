from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippet/<int:pk>/", views.SnippetDetail.as_view()),
    path("userList/", views.UserList.as_view()),
    path("userDetail/<int:pk>/", views.UserDetail.as_view()),
    path("api-auth", include("rest_framework.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
