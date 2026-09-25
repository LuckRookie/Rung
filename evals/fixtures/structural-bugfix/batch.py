from orders import Order


def cancel_batch(orders: list[Order]) -> list[dict]:
    results = []
    for order in orders:
        if order.state == "delivered":
            results.append({"id": order.id, "result": "conflict"})
            continue
        order.state = "cancelled"
        results.append({"id": order.id, "result": "cancelled"})
    return results
