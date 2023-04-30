from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from .serializers import StudentSerializer, StudentInformationSerializer
from .models import Student, StudentInformation
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListBatchAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        batch = self.kwargs['batch']
        queryset = Student.objects.filter(batch=batch)
        return queryset


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'rollNo'


class StudentDestroyAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'rollNo'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'rollNo'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()


# Student Information Section

class StudentInformationCreateAPIView(generics.CreateAPIView):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentInformationSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.student)


class StudentInformationListAPIView(generics.ListAPIView):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentInformationSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StudentInformationListBatchAPIView(generics.ListAPIView):
    serializer_class = StudentInformationSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        batch = self.kwargs['batch']
        queryset = StudentInformation.objects.filter(batch=batch)
        return queryset


class StudentInformationDetailAPIView(generics.RetrieveAPIView):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentInformationSerializer
    lookup_field = 'student__rollNo'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StudentInformationUpdateAPIView(generics.UpdateAPIView):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentInformationSerializer
    lookup_field = 'student__rollNo'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()


class StudentInformationDestroyAPIView(generics.DestroyAPIView):
    queryset = StudentInformation.objects.all()
    serializer_class = StudentInformationSerializer
    lookup_field = 'student__rollNo'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
