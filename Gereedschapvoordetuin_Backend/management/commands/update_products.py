import csv
import json
import re
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from Gereedschapvoordetuin_Backend.models import Product


class Command(BaseCommand):
    help = "Update the products of the supermarkets"

    def add_arguments(self, parser):
        parser.add_argument('-a', '--all', action='store_true', help='Update all markets')

    def handle(self, *args, **options) -> None:
        all = options.get('all', False)
        if all:
            print('=== Updating Talentools ===')
            update_market('talentools')
            print('=== Done Updating Talentools ===')
        else:
            print('Missing argument. Use --all for all markets or type the market name after command')


def update_market(market_name):

    with open(os.path.join(settings.BASE_DIR, "products", (market_name + "_products.csv")), encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        data = list(reader)

        for row in data:
            if row[2] != 'product_name' and row[2] != '':
                try:
                    _, created = Product.objects.update_or_create(
                        product_id=row[1],
                        defaults={
                            'ean_code': row[0] if row[0] != '' else 0,
                            'product_id': row[1],
                            'product_name': row[2],
                            'product_description': row[3],
                            'product_price': row[4].replace("\xa0", ""),
                            'product_image': row[5],
                            'product_weight': row[6],
                            'product_height': row[7],
                            'product_length': row[8],
                            'product_width': row[9],
                            'product_url': row[10],
                            'unit_type': row[11],
                        },
                    )
                except Exception as e:
                    print(e, row[10])
