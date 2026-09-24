# Released rota contract

The supported API is `rota.owner_at(slots, instant)`. A slot is a half-open
interval `[start, end)` with one owner. Lookup returns that owner, or `None`
outside all slots. Input slots must not overlap; invalid intervals raise
`ValueError`. Adjacent intervals are valid and have no uncovered instant.

Consumers are the on-call page and the incident dispatcher. Room reservations
have no released API. Changes to slot ownership must preserve interval and
lookup semantics for both consumers.
