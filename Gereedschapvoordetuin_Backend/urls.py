from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, authentication

from .views import product

schema_view = get_schema_view(
    openapi.Info(
      title="Gereedschapvoordetuin API",
      default_version='v1',
      description="The API for https://www.gereedschapvoordetuin.nl",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[authentication.SessionAuthentication]
)

urlpatterns = [
    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Products
    path('products/', product.get_product, name='get_product'),
    path('search/<path:query>', product.search_product_with_query, name='search_product_with_query'),

    # Django
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
