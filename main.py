# main.py
from dataLoader import load_destinations, load_roads
from greedyAlgorithm import greedy_company_strategy, greedy_driver_strategy

def main():
    # Load data
    destinations = load_destinations("data/destinations.csv")
    roads = load_roads("data/roads.csv")

    depot = "0"   # assume depot node is 0
    capacity = 3  # adjustable

    print("\n=== Company’s Greedy Route ===")
    route_a, profit_a = greedy_company_strategy(depot, destinations, roads, capacity)
    print("Route:", route_a, "Profit:", profit_a)

    print("\n=== Driver’s Greedy Route ===")
    route_b, profit_b = greedy_driver_strategy(depot, destinations, roads, capacity)
    print("Route:", route_b, "Take-home:", profit_b)


if __name__ == "__main__":
    main()
