from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import TouristSpotViewSet
from attraction.api.viewsets import AttractionViewSet
from address.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from evaluations.api.viewsets import EvaluationViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token 


router = routers.DefaultRouter()
router.register('touristspot', TouristSpotViewSet, basename='TouristSpot')
router.register('attractions', AttractionViewSet)
router.register('address', AddressViewSet)
router.register('comments', CommentViewSet)
router.register('evaluations', EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/',obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
