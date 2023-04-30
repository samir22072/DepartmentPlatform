from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', views.FaclutyListAPIView.as_view()),
    path('create/faculty/', views.FacultyCreateAPIView.as_view()),
    path('detail/<facultyId>/', views.FaclutyDetailAPIView.as_view()),
    path('delete/<facultyId>/', views.FacultyDestroyAPIView.as_view()),
    path('update/<facultyId>/', views.FacultyUpdateAPIView.as_view())

]
