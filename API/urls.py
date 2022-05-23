from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('productsbyowner', views.ProductByOwnerViewSet, basename='productsbyowner')

# router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('bookmark', views.RecipeBookmarkView, basename='product-bookmark')

# URLConf
urlpatterns = router.urls + products_router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     path("/bookmarks/", views.RecipeBookmarkView.as_view()),
# ]