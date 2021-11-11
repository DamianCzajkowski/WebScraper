from rest_framework import routers
from apps.scrapper.api.views import ScrapWebsiteViewSet

router = routers.SimpleRouter()

router.register('scrap-webiste', ScrapWebsiteViewSet, 'scrap_website')


urlpatterns = []

urlpatterns += router.urls
