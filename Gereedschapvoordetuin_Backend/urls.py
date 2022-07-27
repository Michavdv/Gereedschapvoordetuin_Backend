from django.urls import include, path

from .views import product


urlpatterns = [
    # Products
    path('products/', product.get_product, name='get_product'),

    # Django
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
