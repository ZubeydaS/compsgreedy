"""
Greedy Route Planner
Author: Emma, Chloe
Assignment: Greedy Algorithm Group Project

Description:
This starter code helps students implement a simple greedy algorithm
for delivery route planning, focusing on:
 - Company’s Greedy Strategy (maximize company profit)
 - Driver’s Greedy Strategy (maximize driver take-home pay)
 - Ethical Modifications (safety, fairness, fatigue, etc.)

Input files:
 - destinations.csv : nodes (place_id, place_name, delivery_fee, tip_estimate)
 - roads.csv : edges (from_id, to_id, travel_cost)
"""

import csv

# ---------------------------------------------------------------------------
# 1. Data structures
# ---------------------------------------------------------------------------

class Place:
    def __init__(self, place_id, name, delivery_fee, tip_estimate):
        self.id = place_id
        self.name = name
        self.delivery_fee = float(delivery_fee)
        self.tip_estimate = float(tip_estimate)

class Road:
    def __init__(self, from_id, to_id, travel_cost):
        self.from_id = from_id
        self.to_id = to_id
        self.travel_cost = float(travel_cost)

# ---------------------------------------------------------------------------
# 2. Load CSV data
# ---------------------------------------------------------------------------

def load_destinations(filename):
    """Load all delivery destinations (nodes)"""
    destinations = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            place = Place(row['id'], row['name'], row['delivery_fee'], row['tip_estimate'])
            destinations[place.id] = place
    return destinations

def load_roads(filename):
    """Load all roads (edges) and return adjacency list"""
    roads = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            a, b, cost = row['from_id'], row['to_id'], float(row['travel_cost'])
            # Create undirected graph (two-way roads)
            roads.setdefault(a, []).append((b, cost))
            roads.setdefault(b, []).append((a, cost))
    return roads

# ---------------------------------------------------------------------------
# 3. Greedy algorithms
# ---------------------------------------------------------------------------

def greedy_company_strategy(current_id, destinations, roads, capacity):
    """
    Company’s greedy algorithm:
    - Choose next customer that maximizes (delivery_fee - travel_cost)
    """
    visited = set([current_id])
    profit = 0.0
    route = [current_id]

    while len(visited) < capacity + 1 and len(visited) <= len(destinations):
        best_next = None
        best_value = float('-inf')

        for neighbor, cost in roads.get(current_id, []):
            if neighbor not in visited:
                value = destinations[neighbor].delivery_fee - cost
                if value > best_value:
                    best_value = value
                    best_next = neighbor

        if best_next is None:
            break  # No more reachable nodes

        visited.add(best_next)
        profit += best_value
        route.append(best_next)
        current_id = best_next

    # Return to depot (simplified cost)
    profit -= roads[route[-1]][0][1] if roads.get(route[-1]) else 0
    return route, profit


def greedy_driver_strategy(current_id, destinations, roads, capacity):
    """
    Driver’s greedy algorithm:
    - Choose next stop that maximizes (tip_estimate - travel_cost)
    """
    visited = set([current_id])
    take_home = 0.0
    route = [current_id]

    while len(visited) < capacity + 1 and len(visited) <= len(destinations):
        best_next = None
        best_value = float('-inf')

        for neighbor, cost in roads.get(current_id, []):
            if neighbor not in visited:
                value = destinations[neighbor].tip_estimate - cost
                if value > best_value:
                    best_value = value
                    best_next = neighbor

        if best_next is None:
            break

        visited.add(best_next)
        take_home += best_value
        route.append(best_next)
        current_id = best_next

    # Cost of returning to depot
    take_home -= roads[route[-1]][0][1] if roads.get(route[-1]) else 0
    return route, take_home


def ethical_rule_strategy(current_id, destinations, roads, capacity, rule="safety"):
    """
    Ethical modification layer:
    Example rules students can test:
     - "safety": avoid roads > 5 miles unless necessary
     - "fairness": every second stop is low-tip if available
     - "fatigue": alternate long and short drives
    """
    # TODO: students implement their own decision rule here
    pass

# ---------------------------------------------------------------------------
# 4. Main execution
# ---------------------------------------------------------------------------

def main():
    # Load data
    destinations = load_destinations("destinations.csv")
    roads = load_roads("roads.csv")

    depot = "0"  # assume ID 0 is depot
    capacity = 3  # example capacity for testing

    print("\n=== Company’s Greedy Route ===")
    route_a, profit_a = greedy_company_strategy(depot, destinations, roads, capacity)
    print("Route:", route_a, "Profit:", profit_a)

    print("\n=== Driver’s Greedy Route ===")
    route_b, profit_b = greedy_driver_strategy(depot, destinations, roads, capacity)
    print("Route:", route_b, "Take-home:", profit_b)

    print("\n=== Ethical Rule Route (to be implemented) ===")
    # route_c, profit_c = ethical_rule_strategy(depot, destinations, roads, capacity, rule="safety")

if __name__ == "__main__":
    main()
