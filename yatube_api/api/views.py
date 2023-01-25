from rest_framework import viewsets
from posts.models import Post, Group, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .permissions import AuthorOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework import mixins


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, AuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly, permissions.IsAuthenticated]

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_user(self):
        return self.request.user

    def get_queryset(self):
        return Follow.objects.filter(user=self.get_user())

    def perform_create(self, serializer):
        serializer.save(user=self.get_user())
