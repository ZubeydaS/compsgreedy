"""
Greedy Algorithm Assignment - Core Classes and Utilities

This file contains the Node and Edge classes, plus helper functions.
Students import from this file but implement their algorithms in student_implementation.py
"""

import math
from typing import List


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
    
    def distance_to(self, other: 'Node') -> float:
        """Calculate Euclidean distance to another node."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __repr__(self):
        depot_str = " (DEPOT)" if self.is_depot else ""
        return (f"Node {self.id}{depot_str}: ({self.x}, {self.y}), "
                f"Fee=${self.delivery_fee:.2f}, Tip=${self.estimated_tip:.2f}, "
                f"Region={self.region}, Priority={self.priority}")


class Edge:
    """
    Represents a road connecting two nodes.
    
    Students can calculate weights using edge.get_distance() or edge.u.distance_to(edge.v)
    
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
        """
        return self.u.distance_to(self.v)
    
    def __repr__(self):
        return f"Edge({self.u.id} <-> {self.v.id})"


def calculate_travel_cost(distance: float, base_cost_per_mile: float = 0.50) -> float:
    """
    Calculate the cost of traveling a given distance.
    
    Students can use this helper function to convert distance into cost.
    
    Args:
        distance (float): Distance to travel
        base_cost_per_mile (float): Cost per unit distance (default: $0.50/mile)
        
    Returns:
        float: Total travel cost
    """
    return distance * base_cost_per_mile


def get_neighbors(node: Node, edges: List[Edge]) -> List[Node]:
    """
    Get all nodes directly connected to the given node via road edges.
    
    Args:
        node (Node): The node to find neighbors for
        edges (List[Edge]): All road Edge objects
        
    Returns:
        List[Node]: List of neighboring nodes connected by roads
    """
    neighbors = []
    for edge in edges:
        if edge.u.id == node.id:
            neighbors.append(edge.v)
        elif edge.v.id == node.id:
            neighbors.append(edge.u)
    return neighbors


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

