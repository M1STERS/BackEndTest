from .api import PersonaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/Personas', PersonaViewSet, 'Personas')
urlpatterns = router.urls