from django.shortcuts import render

from rest_framework import viewsets
from .models import Schools, Students
from rest_framework.response import Response
from .serializers import SchoolsSerializer, StudentsSerializer
from rest_framework import status
from django.http import JsonResponse


class SchoolsViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.all().order_by('sc_name')
    serializer_class = SchoolsSerializer
    paginate_by = 10

    def get(self, request, pk):
        schools = self.get_object(pk)
        serializer = SchoolsSerializer(schools)
        return Response(serializer.data)

    def put(self, request, pk):

        snippet = self.get_object(pk)
        serializer = SchoolsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('st_ident')
    serializer_class = StudentsSerializer
    paginate_by = 10

    def get(self, request, pk):
        students = self.get_object(pk)
        serializer = StudentsSerializer(students)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StudentsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

