from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('', views.StudentListAPIView.as_view()),
    path('<batch>/', views.StudentListBatchAPIView.as_view()),
    path('create/student/', views.StudentCreateAPIView.as_view()),
    path('detail/<rollNo>/', views.StudentDetailAPIView.as_view()),
    path('delete/<rollNo>/', views.StudentDestroyAPIView.as_view()),
    path('update/<rollNo>/', views.StudentUpdateAPIView.as_view()),

    path('information/create/', views.StudentInformationCreateAPIView.as_view()),
    path('information/detail/<student__rollNo>/',
         views.StudentInformationDetailAPIView.as_view()),
    path('information/delete/<student__rollNo>/',
         views.StudentInformationDestroyAPIView.as_view()),

    path('information/<batch>/',
         views.StudentInformationListBatchAPIView.as_view())


]
