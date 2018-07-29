import re


class Orders(object):
    """
        order function
    """

    submission_formats = {
        'IMG': {
            'bundles': {
                10: 800.0,
                5: 450.0,
            },
            'desc': 'Image'
        },
        'FLAC': {
            'bundles': {
                9: 1147.5,
                6: 810.0,
                3: 427.5,
            },
            'desc': 'Audio'
        },
        'VID': {
            'bundles': {
                5: 900.0,
                3: 570.0,
                9: 1530.0,
            },
            'desc': 'Video'
        }
    }
    orders = None

    def __init__(self, orders=None):
        if not orders:
            return None

        self.orders = orders

    def parse_orders(self):
        if not self.orders:  # passed orders should not be empty
            return None

        p = re.compile(r'(\d+)\s(\w+)')

        orders = p.findall(self.orders) or None

        return orders

    def compute_orders(self):
        total_orders = {}

        orders = self.parse_orders()

        # passed orders should not be empty
        if not orders:
            return None

        for order in orders:
            order_code = order[1]
            order_bundle = int(order[0])
            submission_format = self.submission_formats.get(order_code)

            total_orders[order_code] = {}
            total_orders[order_code]['bundles'] = []
            total_orders[order_code]['total_count'] = order_bundle
            total = 0

            for bundle in submission_format['bundles'].keys():
                bundle_details = {}
                amount = submission_format['bundles'].get(bundle)
                count = int(order_bundle / bundle)

                if count:
                    bundle_cost = count * amount

                    bundle_details['bundle'] = bundle
                    bundle_details['price'] = amount
                    bundle_details['count'] = count
                    bundle_details['cost'] = bundle_cost

                    total_orders[order_code]['bundles'].append(bundle_details)
                    total += count * amount

                order_bundle = order_bundle - (count * bundle)

            total_orders[order_code].update({
                'total_price': total
            })

        return total_orders


if __name__ == '__main__':
    orders = Orders(input('Enter order: '))

    if orders.orders:
        for order_code, orders in orders.compute_orders().items():
            total_price = orders.get('total_price')
            total_count = orders.get('total_count')
            bundles = orders.get('bundles')

            print(f'{total_count} {order_code} ${total_price:.2f}')
            for order_bundle in bundles:
                count = order_bundle.get('count')
                bundle = order_bundle.get('bundle')
                cost = order_bundle.get('cost')

                print(f'    {count} x {bundle} ${cost:.2f}')
