from django.urls import path, include

from tweet import views
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('tweets', views.TweetViewSet, basename='tweets')

comment_router = routers.NestedDefaultRouter(router, 'tweets', lookup='tweet')
comment_router.register('comments', views.CommentViewSet, basename='tweet-comments')


urlpatterns = router.urls + comment_router.urls

# [
    # path('', views.TweetList.as_view()),
    # path('<int:pk>/', views.TweetDetails.as_view()),
    # path('', include(router.urls)),
    # path('comments/', views.CommentList.as_view()),
    # path('comments/<int:pk>/', views.CommentDetail.as_view())
# ]

print(router.urls)