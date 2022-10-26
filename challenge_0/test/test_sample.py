import unittest
from sample_lib.sample import Cart
from unittest.mock import patch


class CartTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def assert_for_empty_cart(self):
        self.cart.total()
        self.assertEqual(self.cart.items, [])
        self.assertEqual(self.cart.taxPercent, 18.00)
        self.assertEqual(self.cart.total_value, 0)
        self.assertEqual(self.cart.tax, 0)
        self.assertEqual(self.cart.cart_total, 0)

    def get_printed_cart(self):
        _cart = "\nCart:\n"
        _cart += "\n  1. TestItem - Rs. 9876543.21\n"
        _cart += f"\n    Total:\t\tRs. 9876543.21\n"
        _cart += f"    Tax (18.0%):\tRs. 1777777.78\n"
        _cart += "    -----------------------------------"
        _cart += f"\n    Grand Total:\tRs. 11654320.99\n"
        return _cart

    @patch("builtins.print")
    def test_cart(self, mock_print):
        self.assert_for_empty_cart()
        print(self.cart.__str__())
        mock_print.assert_called_with("Nothing in cart")
        self.cart.add_item("TestItem", 9876543.21)
        print(self.cart.__str__())
        mock_print.assert_called_with(self.get_printed_cart())
        expected = [{"name": "TestItem", "price": 9876543.21}]
        self.assertEqual(self.cart.items, expected)
        self.assertEqual(self.cart.total_value, 9876543.21)
        self.assertEqual(self.cart.tax, 1777777.78)
        self.assertEqual(self.cart.cart_total, 11654320.99)
        self.cart.clear_cart()
        self.assert_for_empty_cart()
