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
    # START YOUR IMPLEMENTATION HERE
    
    # Initialize route with depot and tracking variables
    route = [depot]
    current_node = depot
    visited_customers = set()  # Track visited customer IDs
    total_profit = 0.0
    
    # Get all customer nodes (non-depot nodes)
    customer_nodes = [node for node in nodes if not node.is_depot]
    
    # Continue until all customers are visited
    while len(visited_customers) < len(customer_nodes):
        # Get neighbors of current node
        neighbors = get_neighbors(current_node, edges)
        
        # Filter to unvisited customer neighbors
        unvisited_customer_neighbors = []
        for neighbor in neighbors:
            if not neighbor.is_depot and neighbor.id not in visited_customers:
                unvisited_customer_neighbors.append(neighbor)
        
        # If no unvisited customer neighbors, find the best reachable customer
        if not unvisited_customer_neighbors:
            # Find all unvisited customers and calculate direct distance
            unvisited_customers = [node for node in customer_nodes if node.id not in visited_customers]
            if not unvisited_customers:
                break
                
            # Choose the closest unvisited customer by direct distance
            best_customer = None
            best_profit = float('-inf')
            
            for customer in unvisited_customers:
                distance = current_node.distance_to(customer)
                travel_cost = calculate_travel_cost(distance)
                profit = customer.delivery_fee - travel_cost
                
                if profit > best_profit:
                    best_profit = profit
                    best_customer = customer
            
            if best_customer:
                route.append(best_customer)
                visited_customers.add(best_customer.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_customer))
                total_profit += best_customer.delivery_fee - travel_cost
                current_node = best_customer
        else:
            # Calculate profit for each unvisited customer neighbor
            best_neighbor = None
            best_profit = float('-inf')
            
            for neighbor in unvisited_customer_neighbors:
                distance = current_node.distance_to(neighbor)
                travel_cost = calculate_travel_cost(distance)
                profit = neighbor.delivery_fee - travel_cost
                
                if profit > best_profit:
                    best_profit = profit
                    best_neighbor = neighbor
            
            # Move to the best neighbor
            if best_neighbor:
                route.append(best_neighbor)
                visited_customers.add(best_neighbor.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_neighbor))
                total_profit += best_neighbor.delivery_fee - travel_cost
                current_node = best_neighbor
    
    # Return to depot
    if current_node != depot:
        route.append(depot)
        return_cost = calculate_travel_cost(current_node.distance_to(depot))
        total_profit -= return_cost  # Subtract cost to return
    
    return route, total_profit
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# PART B: DRIVER'S GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_driver_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
    Part B: Implement the driver's greedy algorithm.
    
    Goal: Maximize driver earnings (delivery_fee + estimated_tip - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighboring customer nodes (connected by roads)
    3. Calculate earnings for each: delivery_fee + tip - travel_cost
    4. Choose the neighbor with highest earnings
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total earnings)
        
    TODO: Students implement this function
    """
def greedy_driver_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
    Part B: Implement the driver's greedy algorithm.
    
    Goal: Maximize driver earnings (delivery_fee + estimated_tip - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighboring customer nodes (connected by roads)
    3. Calculate earnings for each: delivery_fee + tip - travel_cost
    4. Choose the neighbor with highest earnings
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total earnings)
        
    TODO: Students implement this function
    """
    # START YOUR IMPLEMENTATION HERE
    
    # Initialize route with depot and tracking variables
    route = [depot]
    current_node = depot
    visited_customers = set()  # Track visited customer IDs
    total_earnings = 0.0
    
    # Get all customer nodes (non-depot nodes)
    customer_nodes = [node for node in nodes if not node.is_depot]
    
    # Continue until all customers are visited
    while len(visited_customers) < len(customer_nodes):
        # Get neighbors of current node
        neighbors = get_neighbors(current_node, edges)
        
        # Filter to unvisited customer neighbors
        unvisited_customer_neighbors = []
        for neighbor in neighbors:
            if not neighbor.is_depot and neighbor.id not in visited_customers:
                unvisited_customer_neighbors.append(neighbor)
        
        # If no unvisited customer neighbors, find the best reachable customer
        if not unvisited_customer_neighbors:
            # Find all unvisited customers and calculate direct distance
            unvisited_customers = [node for node in customer_nodes if node.id not in visited_customers]
            if not unvisited_customers:
                break
                
            # Choose the customer with best earnings by direct distance
            best_customer = None
            best_earnings = float('-inf')
            
            for customer in unvisited_customers:
                distance = current_node.distance_to(customer)
                travel_cost = calculate_travel_cost(distance)
                earnings = customer.delivery_fee + customer.estimated_tip - travel_cost
                
                if earnings > best_earnings:
                    best_earnings = earnings
                    best_customer = customer
            
            if best_customer:
                route.append(best_customer)
                visited_customers.add(best_customer.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_customer))
                earnings = best_customer.delivery_fee + best_customer.estimated_tip - travel_cost
                total_earnings += earnings
                current_node = best_customer
        else:
            # Calculate earnings for each unvisited customer neighbor
            best_neighbor = None
            best_earnings = float('-inf')
            
            for neighbor in unvisited_customer_neighbors:
                distance = current_node.distance_to(neighbor)
                travel_cost = calculate_travel_cost(distance)
                # Driver earnings = delivery fee + tip - travel cost
                earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
                
                if earnings > best_earnings:
                    best_earnings = earnings
                    best_neighbor = neighbor
            
            # Move to the best neighbor
            if best_neighbor:
                route.append(best_neighbor)
                visited_customers.add(best_neighbor.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_neighbor))
                earnings = best_neighbor.delivery_fee + best_neighbor.estimated_tip - travel_cost
                total_earnings += earnings
                current_node = best_neighbor
    
    # Return to depot
    if current_node != depot:
        route.append(depot)
        return_cost = calculate_travel_cost(current_node.distance_to(depot))
        total_earnings -= return_cost  # Subtract cost to return
    
    return route, total_earnings
    
    # END YOUR IMPLEMENTATION

# ============================================================================
# PART C: ETHICAL GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_ethical_route(nodes: List[Node], depot: Node, edges: List[Edge], ethical_rule: str) -> Tuple[List[Node], float]:
    """
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
def greedy_ethical_route(nodes: List[Node], depot: Node, edges: List[Edge], ethical_rule: str) -> Tuple[List[Node], float]:
    """
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
    
    # I'll implement the fairness rule based on the driver's algorithm
    # Fairness rule: Alternate between high-tip (≥$3.00) vs low-tip (<$3.00) areas
    
    if ethical_rule == "fairness":
        # Initialize route with depot and tracking variables
        route = [depot]
        current_node = depot
        visited_customers = set()  # Track visited customer IDs
        total_earnings = 0.0
        
        # Track fairness: True = should prioritize high-tip, False = should prioritize low-tip
        prioritize_high_tip = True
        consecutive_high_tip = 0
        consecutive_low_tip = 0
        
        # Get all customer nodes (non-depot nodes)
        customer_nodes = [node for node in nodes if not node.is_depot]
        
        # Continue until all customers are visited
        while len(visited_customers) < len(customer_nodes):
            # Get neighbors of current node
            neighbors = get_neighbors(current_node, edges)
            
            # Filter to unvisited customer neighbors
            unvisited_customer_neighbors = []
            for neighbor in neighbors:
                if not neighbor.is_depot and neighbor.id not in visited_customers:
                    unvisited_customer_neighbors.append(neighbor)
            
            # If no unvisited customer neighbors, find best reachable customer
            if not unvisited_customer_neighbors:
                unvisited_customers = [node for node in customer_nodes if node.id not in visited_customers]
                if not unvisited_customers:
                    break
                unvisited_customer_neighbors = unvisited_customers
            
            # Separate into high-tip and low-tip neighbors
            high_tip_neighbors = [n for n in unvisited_customer_neighbors if n.estimated_tip >= 3.00]
            low_tip_neighbors = [n for n in unvisited_customer_neighbors if n.estimated_tip < 3.00]
            
            # Calculate earnings with ethical bonuses
            best_neighbor = None
            best_score = float('-inf')
            
            for neighbor in unvisited_customer_neighbors:
                distance = current_node.distance_to(neighbor)
                travel_cost = calculate_travel_cost(distance)
                base_earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
                
                # Apply fairness bonuses
                ethical_bonus = 0
                is_high_tip = neighbor.estimated_tip >= 3.00
                
                # Give bonus based on fairness alternation
                if prioritize_high_tip and is_high_tip:
                    ethical_bonus += 2  # Bonus for high-tip when due
                elif not prioritize_high_tip and not is_high_tip:
                    ethical_bonus += 3  # Larger bonus for low-tip areas (equity)
                
                total_score = base_earnings + ethical_bonus
                
                if total_score > best_score:
                    best_score = total_score
                    best_neighbor = neighbor
            
            # Move to the best neighbor
            if best_neighbor:
                route.append(best_neighbor)
                visited_customers.add(best_neighbor.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_neighbor))
                earnings = best_neighbor.delivery_fee + best_neighbor.estimated_tip - travel_cost
                total_earnings += earnings
                current_node = best_neighbor
                
                # Update fairness tracking
                is_high_tip = best_neighbor.estimated_tip >= 3.00
                if is_high_tip:
                    consecutive_high_tip += 1
                    consecutive_low_tip = 0
                    if consecutive_high_tip >= 2:  # Switch to prioritizing low-tip
                        prioritize_high_tip = False
                else:
                    consecutive_low_tip += 1
                    consecutive_high_tip = 0
                    if consecutive_low_tip >= 1:  # Switch to prioritizing high-tip
                        prioritize_high_tip = True
        
        # Return to depot
        if current_node != depot:
            route.append(depot)
            return_cost = calculate_travel_cost(current_node.distance_to(depot))
            total_earnings -= return_cost
        
        return route, total_earnings
    
    elif ethical_rule == "fatigue":
        # Implement fatigue rule: penalize consecutive long drives (≥15 miles)
        route = [depot]
        current_node = depot
        visited_customers = set()
        total_earnings = 0.0
        last_drive_was_long = False  # Track if previous drive was long (≥15 miles)
        
        customer_nodes = [node for node in nodes if not node.is_depot]
        
        while len(visited_customers) < len(customer_nodes):
            neighbors = get_neighbors(current_node, edges)
            unvisited_customer_neighbors = [n for n in neighbors if not n.is_depot and n.id not in visited_customers]
            
            # If no unvisited customer neighbors, find best reachable customer
            if not unvisited_customer_neighbors:
                unvisited_customers = [node for node in customer_nodes if node.id not in visited_customers]
                if not unvisited_customers:
                    break
                unvisited_customer_neighbors = unvisited_customers
            
            best_neighbor = None
            best_score = float('-inf')
            
            for neighbor in unvisited_customer_neighbors:
                distance = current_node.distance_to(neighbor)
                travel_cost = calculate_travel_cost(distance)
                base_earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
                
                # Apply fatigue considerations
                ethical_modifier = 0
                is_long_drive = distance >= 15.0
                
                if last_drive_was_long and is_long_drive:
                    ethical_modifier -= 10  # Penalize consecutive long drives (safety)
                elif last_drive_was_long and not is_long_drive:
                    ethical_modifier += 3   # Reward short "rest" drives after long ones
                
                total_score = base_earnings + ethical_modifier
                
                if total_score > best_score:
                    best_score = total_score
                    best_neighbor = neighbor
            
            if best_neighbor:
                route.append(best_neighbor)
                visited_customers.add(best_neighbor.id)
                distance = current_node.distance_to(best_neighbor)
                travel_cost = calculate_travel_cost(distance)
                earnings = best_neighbor.delivery_fee + best_neighbor.estimated_tip - travel_cost
                total_earnings += earnings
                current_node = best_neighbor
                
                # Update fatigue tracking
                last_drive_was_long = distance >= 15.0
        
        # Return to depot
        if current_node != depot:
            route.append(depot)
            return_cost = calculate_travel_cost(current_node.distance_to(depot))
            total_earnings -= return_cost
        
        return route, total_earnings
    
    elif ethical_rule == "priority":
        # Implement priority rule: balance urgent vs routine deliveries
        route = [depot]
        current_node = depot
        visited_customers = set()
        total_earnings = 0.0
        urgent_served = 0  # Count of urgent deliveries (priority 1-2)
        routine_served = 0  # Count of routine deliveries (priority 3-5)
        
        customer_nodes = [node for node in nodes if not node.is_depot]
        
        while len(visited_customers) < len(customer_nodes):
            neighbors = get_neighbors(current_node, edges)
            unvisited_customer_neighbors = [n for n in neighbors if not n.is_depot and n.id not in visited_customers]
            
            # If no unvisited customer neighbors, find best reachable customer
            if not unvisited_customer_neighbors:
                unvisited_customers = [node for node in customer_nodes if node.id not in visited_customers]
                if not unvisited_customers:
                    break
                unvisited_customer_neighbors = unvisited_customers
            
            best_neighbor = None
            best_score = float('-inf')
            
            for neighbor in unvisited_customer_neighbors:
                distance = current_node.distance_to(neighbor)
                travel_cost = calculate_travel_cost(distance)
                base_earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
                
                # Apply priority considerations
                ethical_bonus = 0
                is_urgent = neighbor.priority <= 2
                is_routine = neighbor.priority >= 3
                
                # Target ratio: serve 2 urgent for every 1 routine delivery
                # Prevent starvation: +6 bonus for routine after 3+ urgent serves
                if urgent_served >= 3 and routine_served == 0 and is_routine:
                    ethical_bonus += 6  # Prevent routine starvation
                elif urgent_served < 2 * routine_served and is_urgent:
                    ethical_bonus += 2  # Maintain target ratio
                
                total_score = base_earnings + ethical_bonus
                
                if total_score > best_score:
                    best_score = total_score
                    best_neighbor = neighbor
            
            if best_neighbor:
                route.append(best_neighbor)
                visited_customers.add(best_neighbor.id)
                travel_cost = calculate_travel_cost(current_node.distance_to(best_neighbor))
                earnings = best_neighbor.delivery_fee + best_neighbor.estimated_tip - travel_cost
                total_earnings += earnings
                current_node = best_neighbor
                
                # Update priority tracking
                if best_neighbor.priority <= 2:
                    urgent_served += 1
                else:
                    routine_served += 1
        
        # Return to depot
        if current_node != depot:
            route.append(depot)
            return_cost = calculate_travel_cost(current_node.distance_to(depot))
            total_earnings -= return_cost
        
        return route, total_earnings
    
    else:
        # Default to driver's algorithm if unknown rule
        return greedy_driver_route(nodes, depot, edges)
    
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