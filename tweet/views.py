from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tweet
from .serializers import TweetSerializer, CommentSerializer
from .models import Comments
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.filter()
    serializer_class = TweetSerializer


class CommentViewSet(ModelViewSet):
    # queryset = Comments.objects.select_related('tweet').all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.select_related('tweet').filter(tweet_id=self.kwargs['tweet_pk'])

# class TweetList(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class TweetDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#

# class CommentList(ListCreateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentDetail(RetrieveDestroyAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer
