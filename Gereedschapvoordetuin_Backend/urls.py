from django.urls import include, path

from .views import product


urlpatterns = [
    # Products
    path('products/', product.get_product, name='get_product'),
    path('search/<path:query>', product.search_product_with_query, name='search_product_with_query'),
]
