from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('offers', views.offerViewSet, basename='offers')
router.register('offersbyowner', views.offerByOwnerViewSet, basename='offersbyowner')

# router.register('customers', views.CustomerViewSet)

offers_router = routers.NestedDefaultRouter(router, 'offers', lookup='offer')
offers_router.register('comments', views.CommentViewSet, basename='offer-comments')
# offers_router.register('bookmark', views.RecipeBookmarkView, basename='offer-bookmark')
router.register('bookmark', views.RecipeBookmarkView, basename='offer-bookmark')


# URLConf
urlpatterns = router.urls + offers_router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     path("/bookmarks/", views.RecipeBookmarkView.as_view()),
# ]