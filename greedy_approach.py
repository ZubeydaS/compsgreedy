"""
Greedy Algorithm Assignment - Greedy Approach Implementation

You should implement greedy algorithms in this file.
"""

from typing import List, Tuple
from main import Node, Edge, get_neighbors, calculate_travel_cost, print_route_summary


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
    # START YOUR IMPLEMENTATION HERE
    
    # Hints:
    # - Similar to Part A, but now consider tips too
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Calculate earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
    # - Choose the neighbor with the highest earnings at each step
    # - Keep track of total earnings (fees + tips - costs)
    
    # Example modification from Part A:
    # earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
    
   
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# PART C: ETHICAL GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_ethical_route(nodes: List[Node], depot: Node, edges: List[Edge], ethical_rule: str = "fairness") -> Tuple[List[Node], float]:
    """
    Part C: Implement an ethically-modified greedy algorithm.
    
    Modify either the company or driver algorithm to incorporate ethical considerations.
    
    Possible ethical rules:
    - "fairness": Alternate between high-tip and low-tip regions
    - "fatigue": Limit consecutive long-distance drives
    - "priority": Consider delivery priority levels
    - "balance": Ensure all regions get early service
    
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
    
    # Hints:
    # - Start with either your Part A or Part B algorithm as a base
    # - Add ethical considerations to the greedy selection process
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Examples:
    #   * Fairness: Give bonus/penalty based on tip equity
    #   * Fatigue: Penalize long consecutive drives
    #   * Balance: Encourage visiting different regions early
    # - You can modify the scoring function to include ethical factors
    # - Compare results with and without ethical modifications
 
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# TESTING FUNCTIONS
# ============================================================================

def test_mn_data():
    """Test implementations with Minnesota data."""
    try:
        from mn_dataset import MN_NODES, MN_DEPOT, MN_EDGES
        
        print("\n" + "="*60)
        print("TESTING WITH MINNESOTA DATA")
        print("="*60)
        
        print(f"Minnesota nodes: {len(MN_NODES)}")
        print(f"Minnesota edges: {len(MN_EDGES)}")
        print(f"Minnesota depot: {MN_DEPOT}")
        
        # Test Part A on larger dataset
        try:
            route_a_mn, profit_a_mn = greedy_company_route(MN_NODES, MN_DEPOT, MN_EDGES)
            print(f"\nCompany algorithm on MN data: ${profit_a_mn:.2f} profit")
            print(f"Route length: {len(route_a_mn)} stops")
        except NotImplementedError:
            print("\nPart A not implemented for MN testing")
        except Exception as e:
            print(f"\nError in Part A on MN data: {e}")
            
    except ImportError:
        print("\nMinnesota dataset not available for testing")


def main():
    """Main testing function."""
    test_mn_data()


if __name__ == "__main__":
    main()