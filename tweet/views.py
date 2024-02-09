
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from .models import Tweet
from .serializers import TweetSerializer, CommentSerializer
from .models import Comments
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from pagination import DefaultPaginationClass


# Create your views here.

class TweetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPaginationClass
    queryset = Tweet.objects.filter()
    serializer_class = TweetSerializer


class CommentViewSet(ListCreateAPIView, RetrieveDestroyAPIView, GenericViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Comments.objects.select_related('tweet').all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.select_related('tweet').filter(tweet_id=self.kwargs['tweet_pk'])

