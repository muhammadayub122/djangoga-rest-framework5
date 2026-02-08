from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Salom1ViewSet,
    Salom2ViewSet,
    Salom3ViewSet,
    Salom4ViewSet,
    Salom5ViewSet,
)

router = DefaultRouter()
router.register(r"1", Salom1ViewSet)
router.register(r"2", Salom2ViewSet, )
router.register(r"3", Salom3ViewSet, )
router.register(r"4", Salom4ViewSet)
router.register(r"5", Salom5ViewSet)
urlpatterns = [
    path("", include(router.urls)),
]