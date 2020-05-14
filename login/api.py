from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins


from login.serializers import UserSerializer, PostsSerializer
from login.models import Posts

class CreateUserView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    model = get_user_model()
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class CreatePostsView(viewsets.ModelViewSet):
    model = Posts
    serializer_class = PostsSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        

    def get_queryset(self):
        user = self.request.user

        return Posts.objects.filter(user=user)
