from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageActionViewSet,
    ThreadMemberViewSet,
    ThreadViewSet,
    MessageViewSet,
    ThreadActionViewSet,
    ForwardedMessageViewSet,
)

router = DefaultRouter()
router.register("messageaction", MessageActionViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("thread", ThreadViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("message", MessageViewSet)
router.register("threadaction", ThreadActionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
