from rest_framework import routers
from .api import TodoViewSet

router = routers.DefaultRouter()
router.register('api/notes', TodoViewSet, 'notes')

urlpatterns = router.urls
