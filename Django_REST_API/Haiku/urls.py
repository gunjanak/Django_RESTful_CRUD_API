
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import HaikuModelViewSet

router = SimpleRouter()

router.register("",HaikuModelViewSet, basename="posts")
urlpatterns = router.urls