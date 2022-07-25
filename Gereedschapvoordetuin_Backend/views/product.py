from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

import html

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Gereedschapvoordetuin_Backend.models import Product
from Gereedschapvoordetuin_Backend.serializers import ProductSerializer, SearchSerializer

page_param = openapi.Parameter('page', in_=openapi.IN_QUERY, required=True, type=openapi.TYPE_INTEGER)


def get_page_and_queryset(request):
    page = request.GET.get('page')
    amount_per_row = request.GET.get('amount')

    if page and page.isnumeric():
        page = int(page)
    else:
        return {}

    if amount_per_row and amount_per_row.isnumeric():
        amount_per_row = int(amount_per_row)
    else:
        amount_per_row = 5

    queryset = Product.objects.all()

    return {"page": page, "queryset": queryset, "amount_per_row": amount_per_row}


@api_view(['GET'])
def get_product(request):
    """
    Return 25 Products

    The list returns products between a range of ({page} - 1) x 25 and ({page}) x 25

    e.g. page 4 returns items 75-99
    """
    data = get_page_and_queryset(request)
    if not data:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    search_result = {"products": data['queryset'][((data['page'] - 1) * (data['amount_per_row'] * 6)):(
                (data['amount_per_row'] * 6) * data['page'])], "amount": len(data['queryset'])}
    serializer = SearchSerializer(search_result)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_product_with_query(request, query):
    """
    Return 25 Products based on {query}

    The call returns products between a range of ({page} - 1) x 25 and ({page}) x 25

    e.g. page 4 returns items 75-99
    """
    data = get_page_and_queryset(request)
    if not data:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    products = []
    query = remove_special_chars(query.lower())
    for p in data['queryset']:
        if remove_special_chars(p.brand.lower()).find(query) != -1 or remove_special_chars(p.product_name.lower()).find(
                query) != -1:
            products.append(p)

    if not products:
        return Response(status=status.HTTP_204_NO_CONTENT)

    search_result = {"products": products[((data['page'] - 1) * (data['amount_per_row'] * 6)):(
            (data['amount_per_row'] * 6) * data['page'])], "amount": len(products)}
    serializer = SearchSerializer(search_result)
    return Response(serializer.data, status=status.HTTP_200_OK)


def remove_special_chars(string, islower=False):
    # Removes the special characters, html text and when islower is True, the string will be set in lowercase
    return ''.join(filter(str.isalnum, html.unescape(
        str(string)).lower())) if islower else ''.join(
        filter(str.isalnum, html.unescape(str(string))))
