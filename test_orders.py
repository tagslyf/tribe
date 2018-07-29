import unittest

from orders import Orders


class OrdersTestCase(unittest.TestCase):
    """
        Tests for brand_orders.py
    """

    def test_is_valid_orders(self):
        orders = Orders('10 IMG 15 FLAC 13 VID')  # valid order format

        self.assertIsNotNone(orders.parse_orders())

    def test_is_invalid_orders(self):
        # orders = Orders('IMG 10 FLAC 15 VID 13')  # invalid order format
        orders = Orders('IMG 10')  # invalid order format

        self.assertIsNone(orders.parse_orders())

    def test_parse_orders(self):
        orders = Orders('10 IMG').parse_orders()

        code = orders[0][1]
        bundles = int(orders[0][0])

        self.assertEqual(code, 'IMG')
        self.assertEqual(bundles, 10)

    def test_compute_orders(self):
        orders = Orders('10 IMG')
        compute_orders = orders.compute_orders()

        order_code = compute_orders.get('IMG')
        total_amount = order_code.get('total_price')
        total_count = order_code.get('total_count')
        bundles = order_code.get('bundles')[0]
        bundle = bundles.get('bundle')
        price = bundles.get('price')
        count = bundles.get('count')
        cost = bundles.get('cost')

        self.assertIsNotNone(order_code)
        self.assertEqual(total_count, 10)
        self.assertEqual(total_amount, 800.0)
        self.assertEqual(bundle, 10)
        self.assertEqual(price, 800.0)
        self.assertEqual(count, 1)
        self.assertEqual(cost, 800.0)


if __name__ == '__main__':
    unittest.main()
