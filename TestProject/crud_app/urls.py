from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crud_app.views import *


router = DefaultRouter()
router.register('products/crud', ProductCRUDView)


urlpatterns = [
    path('categories/list/', CategoryListView.as_view()),
    path('colors/list/', ColorListView.as_view()),
    path('product/image/cd/', ProductImageView.as_view()),

    path('', include(router.urls)),
]
