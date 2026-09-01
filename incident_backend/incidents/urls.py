from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, IncidentViewSet, ProfilViewSet, CommentaireViewSet
router = DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'profils', ProfilViewSet)
router.register(r'commentaires', CommentaireViewSet)

urlpatterns = router.urls