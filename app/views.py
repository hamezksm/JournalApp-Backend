from rest_framework import viewsets,permissions,status,generics
from rest_framework.response import Response
from .serializers import *
from  .models import User, Journal
from .permissions import *

# Create your views here.

# Class based views for the User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # In case a user want to deete him/herself
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the requesting user is the owner or an administrator
        if instance == request.user or request.user.is_staff:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        # If not authorized, return a forbidden response
        return Response(status=status.HTTP_403_FORBIDDEN)
    
class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]