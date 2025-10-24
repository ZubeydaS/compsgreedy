# Tests for Part A & Part B. Run with: pytest -q
#
# in mn_dataset.py. The checks are:
#   1) Route structure is valid (start/end at depot, all customers exactly once).
#   2) Student total >= expected_total - EPS.
#
#
# If a part raises NotImplementedError, the test fails with a clear message.

import mn_dataset as data
import greedy_approach as stu

EPS = 1e-6  # numerical tolerance for floating-point sums

# === Baked expected totals for the fixed dataset (mn_dataset.py) ===
# These were computed once using the intended greedy rule on this dataset.
EXPECTED_PART_A_TOTAL = 224.4642846982303  # company: fee - travel_cost
EXPECTED_PART_B_TOTAL = 289.48621618098906 # driver: fee + tip - travel_cost


def _assert_route_well_formed(route, depot, all_nodes):
    """Common structural checks for any route."""
    assert isinstance(route, list), "Route must be a list of Node objects."
    assert route[0].id == depot.id, "Route must start at the depot."
    assert route[-1].id == depot.id, "Route must end at the depot."

    customers = [n for n in all_nodes if not n.is_depot]
    visited_ids = [n.id for n in route if not n.is_depot]

    # Every customer appears exactly once.
    assert len(visited_ids) == len(customers), \
        f"Route should visit all {len(customers)} customers exactly once."
    assert len(set(visited_ids)) == len(visited_ids), \
        "Route should not repeat customer nodes."

    # Depot should appear exactly twice (start and end).
    depot_count = sum(1 for n in route if n.is_depot)
    assert depot_count == 2, "Depot should appear exactly at start and end."


def _run_and_check_total(part_name, stu_fn, expected_total):
    """Run a student function and compare against the baked expected total."""
    nodes = data.MN_NODES
    depot = data.MN_DEPOT
    edges = data.MN_EDGES

    route, total = stu_fn(nodes, depot, edges)  # may raise NotImplementedError
    _assert_route_well_formed(route, depot, nodes)

    # Student should meet or exceed expected (allow tiny tolerance)
    assert (total + EPS) >= expected_total, (
        f"{part_name}: Your total ({total:.6f}) should be at least the "
        f"expected baseline ({expected_total:.6f})."
    )


def test_part_a_and_b_against_baseline():
    """
    Validate Part A (company) and Part B (driver) in one go.
    Both must be implemented and meet/exceed the baked baselines.
    """
    # Part A: company's greedy (maximize delivery_fee - travel_cost)
    _run_and_check_total(
        part_name="Part A (Company)",
        stu_fn=stu.greedy_company_route,
        expected_total=EXPECTED_PART_A_TOTAL,
    )

    # Part B: driver's greedy (maximize delivery_fee + tip - travel_cost)
    _run_and_check_total(
        part_name="Part B (Driver)",
        stu_fn=stu.greedy_driver_route,
        expected_total=EXPECTED_PART_B_TOTAL,
    )
