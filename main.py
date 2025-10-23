"""
Greedy Algorithm Assignment - Core Classes and Utilities

This file contains the Node and Edge classes, with helper functions.

You shouldn't need to modify this file.

"""
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
    
    def distance_to(self, other_node) -> float:
        """
        Calculate Euclidean distance to another node.
        
        Args:
            other_node (Node): The target node
            
        Returns:
            float: Euclidean distance between this node and the other node
        """
        return ((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2) ** 0.5
    
    def __repr__(self):
        depot_str = " (DEPOT)" if self.is_depot else ""
        return (f"Node {self.id}{depot_str}: ({self.x}, {self.y}), "
                f"Fee=${self.delivery_fee:.2f}, Tip=${self.estimated_tip:.2f}, "
                f"Region={self.region}, Priority={self.priority}")

class Edge:
    """
    Represents a road connecting two nodes.
    
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