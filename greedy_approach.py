"""
Greedy Algorithm Assignment - Greedy Approach Implementation

You should implement greedy algorithms in this file.
"""

from typing import List, Tuple
from main import Node, Edge, calculate_travel_cost


def get_neighbors(current_node: Node, edges: List[Edge]) -> List[Node]:
    """
    Get all nodes that are directly connected to the current node.
    
    Args:
        current_node (Node): The node to find neighbors for
        edges (List[Edge]): All available edges
        
    Returns:
        List[Node]: List of neighboring nodes
    """
    neighbors = []
    for edge in edges:
        if edge.u.id == current_node.id:
            neighbors.append(edge.v)
        elif edge.v.id == current_node.id:
            neighbors.append(edge.u)
    return neighbors


# ============================================================================
# PART A: COMPANY'S GREEDY ALGORITHM 
# ============================================================================

def greedy_company_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
    Part A: Implement the company's greedy algorithm.
    
    Goal: Maximize company profit (delivery_fee - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighboring customer nodes (connected by roads)
    3. Calculate profit for each: delivery_fee - travel_cost to reach it
    4. Choose the neighbor with highest profit
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit)
        
    TODO: Students implement this function
    """
    visited = set()
    route = [depot]
    current_node = depot
    total_profit = 0.0

    # Mark visited depot 
    visited.add(depot.id)
    # Continuing until all nodes (customers in this case) are visited) 
    customers = []
    for node in nodes:
        if not node.is_depot:
            customers.append(node)

    # visit each customers +1 for depot!
    while len(visited) < len(customers) +1:
        # get possible next stops (unvisited neighbors)
        neighbors = get_neighbors(current, edges)
        next_stops = []
            for n in neighbors:
                if n.id not in visited and n.is_depot == False:
                    next_stops.append(n)
    # If no neighbors found, find the best stop by profit
    if not next_stops:
        break 
    best_next = None
    best_profit = -float('inf')
    
    for neighbor in next_stops:
        #calculating distance and travel costs
        dist = current.distance_to(neighbor)
        cost = calculate_travel_cost(dist)
        # profit = delivery_fee - travel_costs
        profit = neighbor.delivery_fee - cost

    # track the best option
    if profit > best_profit:
        best_profit = profit
        best_next = neighbor
    # moving to the best next stop
    current = best_next
    route.append(current)
    visited.add(current.id)
    total_profit += best_profit

    # return to depot
    return_dist = current.distance_to(depot)
    return_cost = calculate_travel_cost(return_dist)
    total_profit -= return_cost
    route.append(depot)
    
return route, total_profit
                        
            
    """
    # START YOUR IMPLEMENTATION HERE
    
    # Hints:
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Use current_node.distance_to(neighbor) to get distance
    # - Use calculate_travel_cost(distance) to get travel cost
    # - Keep track of visited customers using a set of IDs
    # - Calculate profit = neighbor.delivery_fee - travel_cost
    # - Choose the neighbor with the highest profit at each step
    # - Only consider unvisited customer neighbors (not depot, not already visited)
    # - Don't forget to return to the depot at the end

    raise NotImplementedError("Part A not yet implemented")
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# PART B: DRIVER'S GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_driver_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
  #  Part B: Implement the driver's greedy algorithm.
    
  #  Goal: Maximize driver earnings (delivery_fee + estimated_tip - travel_cost)

      visited = set()
    route = [depot]
    current_node = depot
    total_profit = 0.0

    # Mark visited depot 
    visited.add(depot.id)
    # Continuing until all nodes (customers in this case) are visited) 
    customers = []
    for node in nodes:
        if not node.is_depot:
            customers.append(node)

    # visit each customers +1 for depot!
    while len(visited) < len(customers) +1:
        # get possible next stops (unvisited neighbors)
        neighbors = get_neighbors(current, edges)
        next_stops = []
            for n in neighbors:
                if n.id not in visited and n.is_depot == False:
                    next_stops.append(n)
    # If no neighbors found, find the best stop by profit
    if not next_stops:
        break 
    best_next = None
    best_profit = -float('inf')
    
    for neighbor in next_stops:
        #calculating distance and travel costs
        dist = current.distance_to(neighbor)
        cost = calculate_travel_cost(dist)
        # earnings = delivery fee + estimated tip - travel_cost
        earnings = neighbor.delivery_fee + neighbor.estimated_tip - cost

        if earnings > best_earnings:
            best_earnings = earnings
            best_next = neighbor
            
            current = best_next
            route.append(current)
            visited.add(current.id)
            total_earnings += best_earnings

        #return to depot
        if current != depot:
            return_dist + current_distance_to(depot)
            return_cost + calculate_travel_cost(return_dist)
            total_earnings -= return_cost
            route.append(depot)
        return route, total_earnings
    """
    # START YOUR IMPLEMENTATION HERE

    # Hints:
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Use current_node.distance_to(neighbor) to get distance
    # - Use calculate_travel_cost(distance) to get travel cost
    # - Keep track of visited customers using a set of IDs
    # - Calculate earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
    # - Choose the neighbor with the highest earnings at each step
    # - Only consider unvisited customer neighbors (not depot, not already visited)
    # - Don't forget to return to the depot at the end
    
    raise NotImplementedError("Part B not yet implemented")
    
    # END YOUR IMPLEMENTATION

# ============================================================================
# PART C: ETHICAL GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_ethical_route(nodes: List[Node], depot: Node, edges: List[Edge], ethical_rule: str) -> Tuple[List[Node], float]:
    ""   
    
    Part C: Implement an ethically-modified greedy algorithm.
    
    Modify your code from either Part A or B to incorporate ethical considerations.
    
    Choose ONE ethical rule to implement:
    - "fairness": Alternate between high-tip and low-tip regions
    - "fatigue": Limit consecutive long-distance drives 
    - "priority": Consider delivery priority levels
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        ethical_rule (str): Which ethical rule to apply
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit/earnings)
        
    TODO: Students implement this function with ethical modifications  

    """
    # START YOUR IMPLEMENTATION HERE

    visited = set()
    route = [depot]
    current = depot
    total_earnings = 0.0

    # Choosing fairness rule/tracking if the last stop was high or low tip
    last_was_high_tip = False
    # Starting with false so first stop can be either
    visited.add(depot.id)
    # Mark visited depot 
    visited.add(depot.id)
    # Continuing until all nodes (customers in this case) are visited) 
    customers = []
    for node in nodes:
        if not node.is_depot:
            customers.append(node)

    # visit each customers +1 for depot!
    while len(visited) < len(customers) +1:
        # get possible next stops (unvisited neighbors)
        neighbors = get_neighbors(current, edges)
        next_stops = []
            for n in neighbors:
                if n.id not in visited and n.is_depot == False:
                    next_stops.append(n)
    # If no neighbors found, find the best stop by profit
    if not next_stops:
        break 

    best_next = None
    best_score = -999999.0
    best_earnings = 0.0
for neighbor in next_stops:
    # calculate the best earnings
    dist = current.distance_to(neighbor)
    cost = calculate_travel_cost(dist)
    base_earnings = neighbor.delivery_fee + neighbor.estimated_tip - cost
# Applying fairness rule, just using random tip numbers to be considered low or high
score = base_earnings
is_high_tip = neighbor.estimated_tip >= 3.00
# bonus alternating between high and low tip areas or penalty for serving only same type 
if is_high_tip != last_was_high_tip:
    score += 3.0
else:
    score -=2.0 
# bonus for serving low tip areas
if not is_high_tip and last_was_high_tip
    score += 2.0
if score > best_score:
    best_score = score
    best_next = neighbor
    best_earnings = base_earnings
    best_is_high_tip = is_high_tip

# Move to best next stop
if best_next:
    current = best_next
    route.append(current)
    visited.add(current.id)
    total_earnings += best+earnings
    last_was_high_tip = best_is_high_tip

# return to depot
if current != depot:
    return_dist = current.distance_to(depot)
    return_cost = calculate_travel_cost(return_dist)
    total_earnings -+ return_cost
    route.append(depot)

return route, total_earnings


    
    # Hints:
    # - Start with either your Part A or Part B algorithm as a base
    # - Add ethical considerations to the greedy selection process
    # - Use get_neighbors(current_node, edges) to find connected cities
    # 
    # 
    # FAIRNESS RULE:
    # - Track high-tip (≥$3.00) vs low-tip (<$3.00) areas
    # - Alternate between serving affluent and underserved neighborhoods
    # - Give bonus points: +2 for high-tip when due, +3 for low-tip areas
    # - Research basis: McCoy & Lee (2014) delivery equity studies
    #
    # FATIGUE RULE:
    # - Track consecutive long drives (≥15 miles)
    # - Penalize dangerous consecutive long drives: -10 points
    # - Reward short "rest" drives after long ones: +3 points
    # - Research basis: FMCSA safety studies show crash risk increases
    #
    # PRIORITY RULE:
    # - Balance urgent (priority 1-2) vs routine (priority 3-5) deliveries
    # - Target ratio: serve 2 urgent for every 1 routine delivery
    # - Prevent starvation: +6 bonus for routine after 3+ urgent serves
    # - Research basis: Priority scheduling fairness research
    #
    # You can modify the scoring function to include ethical factors
    # Compare results with and without ethical modifications

    raise NotImplementedError("Part C not yet implemented")
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# RUN FUNCTIONS & FEEDBACKS
# ============================================================================

def run_mn_data():
    """Run implementations with Minnesota data."""
    try:
        from mn_dataset import MN_NODES, MN_DEPOT, MN_EDGES
        
        print("\n" + "="*60)
        print("RUNNING WITH MINNESOTA DATA")
        print("="*60)
        
        print(f"Minnesota nodes: {len(MN_NODES)}")
        print(f"Minnesota edges: {len(MN_EDGES)}")
        print(f"Minnesota depot: {MN_DEPOT}")
        
        # Run Part A - Company's algorithm
        print(f"\n{'='*30} PART A {'='*30}")
        try:
            route_a_mn, profit_a_mn = greedy_company_route(MN_NODES, MN_DEPOT, MN_EDGES)
            print(f"Company algorithm: ${profit_a_mn:.2f} profit")
            print(f"Route length: {len(route_a_mn)} stops")
            print("Route sequence:", [node.id for node in route_a_mn])
        except Exception as e:
            print(f"Error in Part A: {e}")
            
        # Run Part B - Driver's algorithm
        print(f"\n{'='*30} PART B {'='*30}")
        try:
            route_b_mn, earnings_b_mn = greedy_driver_route(MN_NODES, MN_DEPOT, MN_EDGES)
            print(f"Driver algorithm: ${earnings_b_mn:.2f} earnings")
            print(f"Route length: {len(route_b_mn)} stops")
            print("Route sequence:", [node.id for node in route_b_mn])
        except Exception as e:
            print(f"Error in Part B: {e}")
            
        # Run Part C - Ethical algorithms
        print(f"\n{'='*30} PART C {'='*30}")
        ethical_rules = ["fairness", "fatigue", "priority"]
        
        for rule in ethical_rules:
            try:
                route_c_mn, earnings_c_mn = greedy_ethical_route(MN_NODES, MN_DEPOT, MN_EDGES, rule)
                print(f"Ethical algorithm ({rule}): ${earnings_c_mn:.2f} earnings")
                print(f"Route length: {len(route_c_mn)} stops")
                print("Route sequence:", [node.id for node in route_c_mn])
                
                # Compare with standard driver algorithm
                difference = earnings_c_mn - earnings_b_mn
                print(f"Difference from standard driver: ${difference:.2f}")
                
                # Analyze ethical impact
                if rule == "fairness":
                    analyze_fairness_impact(route_c_mn, MN_NODES)
                elif rule == "fatigue":
                    analyze_fatigue_impact(route_c_mn)
                elif rule == "priority":
                    analyze_priority_impact(route_c_mn, MN_NODES)
                print()
            except Exception as e:
                print(f"Error in Part C ({rule}): {e}")
                
    except ImportError:
        print("\n MN Dataset not linked properly")


def analyze_fairness_impact(route, nodes):
    """Analyze how the fairness rule affected tip distribution."""
    customer_route = [node for node in route if not node.is_depot]
    high_tip_count = sum(1 for node in customer_route if node.estimated_tip >= 3.00)
    low_tip_count = len(customer_route) - high_tip_count
    
    print(f"  Fairness Impact: {high_tip_count} high-tip areas, {low_tip_count} low-tip areas served")
    
    # Check alternation pattern
    alternations = 0
    for i in range(1, len(customer_route)):
        prev_high = customer_route[i-1].estimated_tip >= 3.00
        curr_high = customer_route[i].estimated_tip >= 3.00
        if prev_high != curr_high:
            alternations += 1
    print(f"  Alternation score: {alternations} tip-level changes in route")


def analyze_fatigue_impact(route):
    """Analyze how the fatigue rule affected drive distances."""
    long_drives = 0
    consecutive_long = 0
    max_consecutive_long = 0
    current_consecutive = 0
    
    for i in range(1, len(route)):
        distance = route[i-1].distance_to(route[i])
        if distance >= 15.0:
            long_drives += 1
            current_consecutive += 1
            max_consecutive_long = max(max_consecutive_long, current_consecutive)
        else:
            current_consecutive = 0
            
    print(f"  Fatigue Impact: {long_drives} long drives (≥15 miles)")
    print(f"  Maximum consecutive long drives: {max_consecutive_long}")


def analyze_priority_impact(route, nodes):
    """Analyze how the priority rule affected delivery order."""
    customer_route = [node for node in route if not node.is_depot]
    urgent_count = sum(1 for node in customer_route if node.priority <= 2)
    routine_count = len(customer_route) - urgent_count
    
    print(f"  Priority Impact: {urgent_count} urgent, {routine_count} routine deliveries")
    
    # Check if urgent deliveries come first
    urgent_positions = [i for i, node in enumerate(customer_route) if node.priority <= 2]
    avg_urgent_position = sum(urgent_positions) / len(urgent_positions) if urgent_positions else 0
    print(f"  Average urgent delivery position: {avg_urgent_position:.1f} out of {len(customer_route)}")


def main():
    """Main Runnning function."""
    run_mn_data()


if __name__ == "__main__":
    main()
