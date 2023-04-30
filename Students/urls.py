from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListAPIView.as_view()),
    path('<batch>', views.StudentListBatchAPIView.as_view()),
    path('create', views.StudentCreateAPIView.as_view()),
    path('<rollNo>', views.StudentDetailAPIView.as_view()),
    path('delete/<rollNo>', views.StudentDestroyAPIView.as_view()),
    path('update/<rollNo>', views.StudentUpdateAPIView.as_view()),

    path('information/create', views.StudentInformationCreateAPIView.as_view()),
    path('information/<rollNo>', views.StudentInformationDetailAPIView.as_view()),
    path('information/delete/<rollNo>',
         views.StudentInformationDestroyAPIView.as_view()),

    path('information/<batch>',
         views.StudentInformationListBatchAPIView.as_view())


]
