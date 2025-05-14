from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    # List all code snippets or create new
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        # Retrieve, Update or Delete
        # check if pk instance exists or not
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = SnippetSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rec = self.get_object(pk)
        serializer = SnippetSerializer(rec, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rec = self.get_object(pk)
        rec.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
