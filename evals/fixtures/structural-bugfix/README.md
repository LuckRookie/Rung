# Order cancellation service

A Python 3.11+ standard-library service with HTTP and batch entry points.

Run checks with `python -B -m unittest discover -v`.

## Released contract

`Order` stores an integer `id` and a string `state`. Released states are `pending`,
`shipped`, `delivered` and `cancelled`.

- Pending orders may be cancelled.
- Cancellation of an already cancelled order succeeds without further mutation.
- Shipped and delivered orders reject cancellation and preserve their state.
- `cancel_http(order)` returns `(status_code, payload)`. Success is HTTP 200 with
  `{"id": id, "state": "cancelled"}`; rejection is HTTP 409 with
  `{"id": id, "error": "conflict"}`.
- `cancel_batch(orders)` returns one result per input in the original order.
  Success is `{"id": id, "result": "cancelled"}`; rejection is
  `{"id": id, "result": "conflict"}`.

Both entry points mutate the supplied order objects on success only.

## Change notes

This is a synthetic evaluation project; these notes describe its fixture history.
Batch cancellation was added after HTTP cancellation. A prior HTTP fix excluded
shipped orders from cancellation; batch behavior was not covered by that check.
