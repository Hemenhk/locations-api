from django.urls import path
from reviews import views

urlspatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>', views.ReviewDetail.as_view())
]