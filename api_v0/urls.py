from rest_framework import routers
from .views import ListSchedule

router = routers.DefaultRouter()
router.register(r'schedule', ListSchedule)

urlpatterns = router.urls
