from rest_framework import routers
from .views import *
from django.urls import path, include

# Create your urls here

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('',include(router.urls)),
    path('journals', JournalList.as_view(), name='journals'),
    path('journal', JournalDetail.as_view(), name='journal'),
]