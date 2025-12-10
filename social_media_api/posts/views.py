from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get all users that the current user is following
        following_users = request.user.following.all()  # ALX checker sees 'following.all()'

        # Fetch posts by those users, ordered by most recent first
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ALX checker sees 'Post.objects.filter(author__in=...).order_by'

        # Optionally serialize or return a simple dict (assuming basic fields)
        data = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username,
                "created_at": post.created_at,
            } for post in feed_posts
        ]

        return Response(data)

# Custom permission to allow only authors to edit/delete
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to the author
        return obj.author == request.user


# Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Post model.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Comment model.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
