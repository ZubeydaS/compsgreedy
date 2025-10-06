# The code need to be written by students. 
# Assignment codes!

def greedy_company_strategy(current_id, destinations, roads, capacity):
    """
    Part A: Company’s greedy algorithm
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
            break

        visited.add(best_next)
        profit += best_value
        route.append(best_next)
        current_id = best_next

    return route, profit


def greedy_driver_strategy(current_id, destinations, roads, capacity):
    """
    Part B: Driver’s greedy algorithm
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

    return route, take_home
