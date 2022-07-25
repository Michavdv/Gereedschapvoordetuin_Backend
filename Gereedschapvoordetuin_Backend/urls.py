from django.urls import include, path, re_path
from rest_framework_swagger.views import get_swagger_view

from .views import product

schema_view = get_swagger_view(
      title="Gereedschapvoordetuin API"
)

urlpatterns = [
    # Swagger
    re_path(r'^$', schema_view),

    # Products
    path('products/', product.get_product, name='get_product'),
    path('search/<path:query>', product.search_product_with_query, name='search_product_with_query'),

    # Django
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
