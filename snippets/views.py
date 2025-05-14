from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    # List all code snippets or create new

    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    # Retrieve, Update or Delete
    # check if pk instance exists or not
    try:
        instance = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(instance)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SnippetSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
