from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.scrapper.models import Scrapper


class ScrapWebsiteViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          GenericViewSet):
    def get_queryset(self):
        return Scrapper.objects.all()
