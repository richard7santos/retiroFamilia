from django.urls import path
from core.views import UserCreate, UserProfileUpdate

urlpatterns = [
    path('update/', UserProfileUpdate.as_view(), name='update'),
    path('register/', UserCreate.as_view(), name='register'),

]
