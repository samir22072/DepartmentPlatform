from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from .serializers import FacultySerializer
from .models import Faculty
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class FacultyCreateAPIView(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class FaclutyListAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class FaclutyDetailAPIView(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'facultyId'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class FacultyDestroyAPIView(generics.DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'facultyId'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class FacultyUpdateAPIView(generics.UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'facultyId'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
