from django.urls import path
from . import views

urlpatterns = [
    path('',views.FaclutyListAPIView.as_view()),
    path('create',views.FacultyCreateAPIView.as_view()),
    path('<facultyId>',views.FaclutyDetailAPIView.as_view()),
    path('delete/<facultyId>',views.FacultyDestroyAPIView.as_view()),
    path('update/<facultyId>',views.FacultyUpdateAPIView.as_view())
    
]