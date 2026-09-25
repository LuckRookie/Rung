import unittest

from batch import cancel_batch
from http_api import cancel_http
from orders import Order


class CancellationTests(unittest.TestCase):
    def test_http_pending(self):
        order = Order(1, "pending")
        self.assertEqual(cancel_http(order), (200, {"id": 1, "state": "cancelled"}))
        self.assertEqual(order.state, "cancelled")

    def test_http_shipped(self):
        order = Order(2, "shipped")
        self.assertEqual(cancel_http(order), (409, {"id": 2, "error": "conflict"}))
        self.assertEqual(order.state, "shipped")

    def test_batch_pending_and_delivered(self):
        orders = [Order(1, "pending"), Order(2, "delivered")]
        self.assertEqual(
            cancel_batch(orders),
            [{"id": 1, "result": "cancelled"}, {"id": 2, "result": "conflict"}],
        )
        self.assertEqual([order.state for order in orders], ["cancelled", "delivered"])

    def test_cancelled_is_idempotent(self):
        self.assertEqual(
            cancel_http(Order(3, "cancelled")), (200, {"id": 3, "state": "cancelled"})
        )
        self.assertEqual(
            cancel_batch([Order(3, "cancelled")]), [{"id": 3, "result": "cancelled"}]
        )


if __name__ == "__main__":
    unittest.main()
