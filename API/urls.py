from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('productsbyowner', views.ProductByOwnerViewSet, basename='productsbyowner')

# router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)