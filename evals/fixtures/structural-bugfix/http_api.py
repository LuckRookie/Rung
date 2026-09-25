from orders import Order


def cancel_http(order: Order) -> tuple[int, dict]:
    if order.state not in {"pending", "cancelled"}:
        return 409, {"id": order.id, "error": "conflict"}
    order.state = "cancelled"
    return 200, {"id": order.id, "state": order.state}
