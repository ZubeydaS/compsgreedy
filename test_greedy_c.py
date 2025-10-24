# Test for Part C. Run with: pytest -q
#
# Students implement one of: "fairness", "fatigue", or "priority".
# This test:
#   1) Gets a baseline route:
#        - Prefer student's Part B (driver) route if implemented;
#        - Otherwise, use a baked baseline route for this dataset.
#   2) Calls greedy_ethical_route for each rule name.
#   3) Passes if ANY one rule returns a valid route AND shows meaningful impact
#      vs the baseline according to that rule's metric.

import mn_dataset as data
import greedy_approach as stu

# === Baked baseline for this dataset (driver rule) ===
# Computed once with the intended Part B greedy on mn_dataset.py.
# Used only if the student's Part B is not implemented.
_BAKED_BASELINE_ROUTE_IDS = [
    0, 1, 10, 9, 8, 6, 7, 5, 24, 2, 3, 17, 18, 19, 23, 22, 21, 16, 13, 14, 15, 12, 11, 20, 4, 0
]

def _nodes_by_id(nodes):
    return {n.id: n for n in nodes}

def _rebuild_route_from_ids(nodes, ids):
    m = _nodes_by_id(nodes)
    return [m[i] for i in ids]

def _assert_route_well_formed(route, depot, all_nodes):
    assert route[0].id == depot.id and route[-1].id == depot.id, \
        "Ethical route must start and end at the depot."
    customers = [n for n in all_nodes if not n.is_depot]
    visited_ids = [n.id for n in route if not n.is_depot]
    assert len(visited_ids) == len(customers), \
        "Ethical route must visit every customer exactly once."
    assert len(set(visited_ids)) == len(visited_ids), \
        "Ethical route must not repeat customers."
    assert sum(1 for n in route if n.is_depot) == 2, \
        "Depot should appear exactly at the start and end."


def _is_high_tip(node):
    return node.estimated_tip >= 3.00


def _alternations_tip(route):
    customers = [n for n in route if not n.is_depot]
    if len(customers) < 2:
        return 0
    flips = 0
    for i in range(1, len(customers)):
        if _is_high_tip(customers[i]) != _is_high_tip(customers[i - 1]):
            flips += 1
    return flips


def _long_drive_stats(route, threshold=15.0):
    """Returns (num_long, max_consecutive_long) for this route distance profile."""
    num_long = 0
    max_consec = 0
    cur = 0
    for i in range(1, len(route)):
        d = route[i - 1].distance_to(route[i])
        is_long = d >= threshold
        if is_long:
            num_long += 1
            cur += 1
            max_consec = max(max_consec, cur)
        else:
            cur = 0
    return num_long, max_consec


def _avg_urgent_position(route):
    """Average position (0-based among customers only) for urgent (priority <= 2)."""
    customers = [n for n in route if not n.is_depot]
    positions = [i for i, n in enumerate(customers) if n.priority <= 2]
    if not positions:
        return float("inf")  # if no urgent nodes exist, treat as worst
    return sum(positions) / len(positions)


def _get_baseline_route(nodes, depot, edges):
    """Prefer student's Part B; otherwise use baked baseline route."""
    try:
        base_route, _ = stu.greedy_driver_route(nodes, depot, edges)
        _assert_route_well_formed(base_route, depot, nodes)
        return base_route
    except NotImplementedError:
        # Fall back to baked baseline (same dataset, deterministic)
        return _rebuild_route_from_ids(nodes, _BAKED_BASELINE_ROUTE_IDS)


def test_part_c_accepts_any_single_ethical_factor():
    nodes = data.MN_NODES
    depot = data.MN_DEPOT
    edges = data.MN_EDGES

    base_route = _get_baseline_route(nodes, depot, edges)
    _assert_route_well_formed(base_route, depot, nodes)

    base_alternations = _alternations_tip(base_route)
    base_num_long, base_max_consec_long = _long_drive_stats(base_route)
    base_avg_urgent = _avg_urgent_position(base_route)

    rules = ["fairness", "fatigue", "priority"]
    passed_any = False
    reasons = []

    for rule in rules:
        try:
            eth_route, _ = stu.greedy_ethical_route(nodes, depot, edges, rule)
        except NotImplementedError:
            reasons.append(f"{rule}: NotImplementedError raised (unimplemented).")
            continue
        except Exception as e:
            reasons.append(f"{rule}: raised {type(e).__name__} - {e}")
            continue

        # Structural validity
        try:
            _assert_route_well_formed(eth_route, depot, nodes)
        except AssertionError as e:
            reasons.append(f"{rule}: route invalid - {e}")
            continue

        # Detect impact relative to baseline depending on the rule.
        impact = False

        if rule == "fairness":
            alt = _alternations_tip(eth_route)
            order_differs = [n.id for n in eth_route] != [n.id for n in base_route]
            if alt > base_alternations or order_differs:
                impact = True
            else:
                reasons.append(f"{rule}: no clear fairness impact (alt {alt} <= base {base_alternations}).")

        elif rule == "fatigue":
            num_long, max_consec = _long_drive_stats(eth_route)
            if (num_long < base_num_long) or (max_consec < base_max_consec_long):
                impact = True
            else:
                reasons.append(
                    f"{rule}: fatigue metrics not improved "
                    f"(long {num_long}/{base_num_long}, "
                    f"max_consec {max_consec}/{base_max_consec_long})."
                )

        elif rule == "priority":
            avg_u = _avg_urgent_position(eth_route)
            if avg_u < base_avg_urgent:
                impact = True
            else:
                reasons.append(
                    f"{rule}: urgent deliveries not earlier on average "
                    f"(avg {avg_u:.2f} vs base {base_avg_urgent:.2f})."
                )

        if impact:
            passed_any = True
            break  # We only need one ethical rule to show impact.

    assert passed_any, (
        "Part C: None of the ethical-rule runs showed a clear impact vs. baseline.\n"
        "Details:\n- " + "\n- ".join(reasons)
    )
