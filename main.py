"""
Greedy Algorithm Assignment - Delivery Route Planning
Starter Code

You should implement the greedy logic in:
- greedyPartA.py (Company's perspective)
- greedyPartB.py (Driver's perspective)  
- greedyPartC.py (Ethical modifications)
"""

import math
from typing import List, Tuple, Optional


class Node:
    """
    Represents a destination (customer location or depot).
    
    Attributes:
        id (int): Unique identifier for the node
        x (float): X-coordinate of the location
        y (float): Y-coordinate of the location
        delivery_fee (float): Fee earned for delivering to this location
        estimated_tip (float): Expected tip from this customer
        region (str): Region type ('downtown', 'suburban', 'rural')
        priority (int): Priority level (1=highest, 5=lowest)
        is_depot (bool): Whether this is the starting depot
    """
    
    def __init__(self, node_id: int, x: float, y: float, 
                 delivery_fee: float = 0.0, estimated_tip: float = 0.0,
                 region: str = "suburban", priority: int = 3, 
                 is_depot: bool = False):
        self.id = node_id
        self.x = x
        self.y = y
        self.delivery_fee = delivery_fee
        self.estimated_tip = estimated_tip
        self.region = region
        self.priority = priority
        self.is_depot = is_depot
    
    def __repr__(self):
        depot_str = " (DEPOT)" if self.is_depot else ""
        return (f"Node {self.id}{depot_str}: ({self.x}, {self.y}), "
                f"Fee=${self.delivery_fee:.2f}, Tip=${self.estimated_tip:.2f}, "
                f"Region={self.region}, Priority={self.priority}")


class Edge:
    """
    Represents a road connecting two nodes.
    
    Note: Edge weights are NOT stored. Students must calculate them
    based on node attributes (e.g., distance, travel cost).
    
    Attributes:
        u (Node): First endpoint
        v (Node): Second endpoint
    """
    
    def __init__(self, u: Node, v: Node):
        self.u = u
        self.v = v
    
    def get_distance(self) -> float:
        """
        Calculate Euclidean distance between the two nodes.
        
        Returns:
            float: Distance between nodes u and v
            
        TODO for students: You may want to use this in your greedy algorithm
        to calculate travel costs.
        """
        return math.sqrt((self.u.x - self.v.x)**2 + (self.u.y - self.v.y)**2)
    
    def __repr__(self):
        return f"Edge({self.u.id} <-> {self.v.id})"


class Graph:
    """
    Represents the delivery network as a graph.
    
    Attributes:
        nodes (List[Node]): All destinations including depot
        edges (List[Edge]): All roads connecting destinations
        depot (Node): The starting/ending depot location
    """
    
    def __init__(self):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []
        self.depot: Optional[Node] = None
    
    def add_node(self, node: Node):
        """Add a node to the graph."""
        self.nodes.append(node)
        if node.is_depot:
            self.depot = node
    
    def add_edge(self, u: Node, v: Node):
        """Add an edge between two nodes."""
        self.edges.append(Edge(u, v))
    
    def get_neighbors(self, node: Node) -> List[Node]:
        """
        Get all nodes directly connected to the given node.
        
        Args:
            node (Node): The node to find neighbors for
            
        Returns:
            List[Node]: List of neighboring nodes
        """
        neighbors = []
        for edge in self.edges:
            if edge.u.id == node.id:
                neighbors.append(edge.v)
            elif edge.v.id == node.id:
                neighbors.append(edge.u)
        return neighbors
    
    def get_edge(self, u: Node, v: Node) -> Optional[Edge]:
        """
        Find the edge connecting two nodes.
        
        Args:
            u (Node): First node
            v (Node): Second node
            
        Returns:
            Optional[Edge]: The edge if it exists, None otherwise
        """
        for edge in self.edges:
            if (edge.u.id == u.id and edge.v.id == v.id) or \
               (edge.v.id == u.id and edge.u.id == v.id):
                return edge
        return None
    
    def __repr__(self):
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"


def calculate_travel_cost(distance: float, base_cost_per_mile: float = 0.50) -> float:
    """
    Calculate the cost of traveling a given distance.
    
    This is a helper function students can use to convert distance into cost.
    
    Args:
        distance (float): Distance to travel
        base_cost_per_mile (float): Cost per unit distance (default: $0.50/mile)
        
    Returns:
        float: Total travel cost
        
    Note: Students may modify this function or create their own cost calculation
    based on different factors (e.g., region-based tolls, time of day).
    """
    return distance * base_cost_per_mile


def create_sample_graph() -> Graph:
    """
    Create a sample graph for testing.
    
    This creates a small delivery network with one depot and several customers.
    Students can use this to test their algorithms.
    
    Returns:
        Graph: A sample delivery network
    """
    g = Graph()
    
    # Create depot (node 0)
    depot = Node(0, 0, 0, delivery_fee=0, estimated_tip=0, 
                 region="downtown", is_depot=True)
    g.add_node(depot)
    
    # Create customer nodes
    customers = [
        Node(1, 3, 4, delivery_fee=10.0, estimated_tip=3.0, region="downtown", priority=1),
        Node(2, 8, 1, delivery_fee=12.0, estimated_tip=2.0, region="suburban", priority=2),
        Node(3, 5, 9, delivery_fee=15.0, estimated_tip=5.0, region="rural", priority=1),
        Node(4, 10, 7, delivery_fee=8.0, estimated_tip=1.5, region="suburban", priority=3),
        Node(5, 2, 8, delivery_fee=11.0, estimated_tip=4.0, region="downtown", priority=2),
    ]
    
    for customer in customers:
        g.add_node(customer)
    
    # Create edges (fully connected graph for simplicity)
    # In a real scenario, not all locations would be directly connected
    for i, node1 in enumerate(g.nodes):
        for node2 in g.nodes[i+1:]:
            g.add_edge(node1, node2)
    
    return g


def print_route_summary(route: List[Node], total_profit: float, total_cost: float):
    """
    Print a formatted summary of the delivery route.
    
    Args:
        route (List[Node]): The sequence of nodes visited
        total_profit (float): Total profit/earnings from the route
        total_cost (float): Total travel cost
    """
    print("\n" + "="*60)
    print("ROUTE SUMMARY")
    print("="*60)
    print(f"Route: {' -> '.join(str(node.id) for node in route)}")
    print(f"\nTotal Travel Cost: ${total_cost:.2f}")
    print(f"Total Profit/Earnings: ${total_profit:.2f}")
    print("="*60 + "\n")


# ============================================================================
# STUDENT IMPLEMENTATION SECTION
# ============================================================================

def greedy_company_route(graph: Graph) -> Tuple[List[Node], float]:
    """
    Part A: Implement the company's greedy algorithm.
    
    Goal: Maximize company profit (delivery_fee - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighbors
    3. Calculate profit for each: delivery_fee - travel_cost to reach it
    4. Choose the neighbor with highest profit
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        graph (Graph): The delivery network
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit)
        
    TODO: Students implement this function
    """
    # START YOUR IMPLEMENTATION HERE

    # END YOUR IMPLEMENTATION


def greedy_driver_route(graph: Graph) -> Tuple[List[Node], float]:
    """
    Part B: Implement the driver's greedy algorithm.
    
    Goal: Maximize driver earnings (delivery_fee + estimated_tip - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighbors
    3. Calculate earnings for each: delivery_fee + tip - travel_cost
    4. Choose the neighbor with highest earnings
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        graph (Graph): The delivery network
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total earnings)
        
    TODO: Students implement this function
    """
    # START YOUR IMPLEMENTATION HERE
    
    # END YOUR IMPLEMENTATION


def greedy_ethical_route(graph: Graph, ethical_rule: str = "fairness") -> Tuple[List[Node], float]:
    """
    Part C: Implement an ethically-modified greedy algorithm.
    
    Modify either the company or driver algorithm to incorporate ethical considerations.
    
    Possible ethical rules:
    - "fairness": Alternate between high-tip and low-tip regions
    - "fatigue": Limit consecutive long-distance drives
    - "priority": Consider delivery priority levels
    - "balance": Ensure all regions get early service
    
    Args:
        graph (Graph): The delivery network
        ethical_rule (str): Which ethical rule to apply
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit/earnings)
        
    TODO: Students implement this function with ethical modifications
    """
    # START YOUR IMPLEMENTATION HERE
 
    # END YOUR IMPLEMENTATION


# ============================================================================
# TESTING AND MAIN
# ============================================================================

def main():
    """
    Main function to test the implementations.
    
    Students should run this to test their greedy algorithms.
    """
    print("Creating sample delivery network...")
    graph = create_sample_graph()
    
    print(f"\n{graph}")
    print(f"Depot: {graph.depot}\n")
    
    print("Customers:")
    for node in graph.nodes:
        if not node.is_depot:
            print(f"  {node}")
    
    print("\n" + "="*60)
    print("TESTING PART A: Company's Greedy Algorithm")
    print("="*60)
    try:
        route_a, profit_a = greedy_company_route(graph)
        print_route_summary(route_a, profit_a, 0)  # Students calculate cost in function
    except NotImplementedError:
        print("Part A not yet implemented.\n")
    
    print("="*60)
    print("TESTING PART B: Driver's Greedy Algorithm")
    print("="*60)
    try:
        route_b, earnings_b = greedy_driver_route(graph)
        print_route_summary(route_b, earnings_b, 0)  # Students calculate cost in function
    except NotImplementedError:
        print("Part B not yet implemented.\n")
    
    print("="*60)
    print("TESTING PART C: Ethical Greedy Algorithm")
    print("="*60)
    try:
        route_c, result_c = greedy_ethical_route(graph, ethical_rule="fairness")
        print_route_summary(route_c, result_c, 0)  # Students calculate cost in function
    except NotImplementedError:
        print("Part C not yet implemented.\n")


if __name__ == "__main__":
    main()