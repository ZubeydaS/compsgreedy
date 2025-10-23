"""
Greedy Algorithm Assignment - Minnesota Cities Dataset 

This file include list of Nodes of MN cities and list of Edges of simplfied Roads.

You shouldn't need to modify this file.
"""
from main import Node, Edge
from typing import List

# === Minnesota city nodes (with attributes) ===================================
MN_NODES = [
    # Depot
    Node(0, 0.0, 0.0, delivery_fee=0.00, estimated_tip=0.00, 
         region="downtown", priority=1, is_depot=True),  # Minneapolis
    
    # Twin Cities Core
    Node(1, 10.0, -2.0, delivery_fee=12.50, estimated_tip=4.00, 
         region="downtown", priority=2, is_depot=False),  # St Paul
    Node(2, -4.0, -6.0, delivery_fee=11.40, estimated_tip=3.60, 
         region="downtown", priority=2, is_depot=False),  # Edina
    Node(3, -2.0, -8.0, delivery_fee=10.75, estimated_tip=3.00, 
         region="downtown", priority=3, is_depot=False),  # Bloomington
    Node(4, 5.0, 3.0, delivery_fee=10.30, estimated_tip=2.60, 
         region="downtown", priority=3, is_depot=False),  # Roseville
    
    # Northern Suburbs
    Node(5, -6.0, 6.0, delivery_fee=12.40, estimated_tip=3.00, 
         region="suburban", priority=3, is_depot=False),  # Maple Grove
    Node(6, 4.0, 10.0, delivery_fee=11.20, estimated_tip=2.90, 
         region="suburban", priority=3, is_depot=False),  # Blaine
    Node(7, -3.0, 9.0, delivery_fee=11.50, estimated_tip=2.70, 
         region="suburban", priority=4, is_depot=False),  # Anoka
    
    # Eastern Cities
    Node(8, 15.0, 10.0, delivery_fee=14.80, estimated_tip=2.60, 
         region="rural", priority=3, is_depot=False),  # Forest Lake
    Node(9, 20.0, 3.0, delivery_fee=14.50, estimated_tip=2.50, 
         region="rural", priority=3, is_depot=False),  # Stillwater
    Node(10, 15.0, -1.0, delivery_fee=13.10, estimated_tip=3.30, 
         region="suburban", priority=2, is_depot=False),  # Woodbury
    Node(11, 13.0, -6.0, delivery_fee=12.90, estimated_tip=3.20, 
         region="suburban", priority=3, is_depot=False),  # Cottage Grove
    
    # Southern Cities
    Node(12, 3.0, -10.0, delivery_fee=11.80, estimated_tip=3.10, 
         region="suburban", priority=2, is_depot=False),  # Eagan
    Node(13, 1.0, -12.0, delivery_fee=11.90, estimated_tip=3.10, 
         region="suburban", priority=3, is_depot=False),  # Burnsville
    Node(14, 2.0, -13.0, delivery_fee=12.70, estimated_tip=3.20, 
         region="suburban", priority=3, is_depot=False),  # Apple Valley
    Node(15, 5.0, -14.0, delivery_fee=12.40, estimated_tip=3.10, 
         region="suburban", priority=3, is_depot=False),  # Rosemount
    Node(16, 1.0, -16.0, delivery_fee=13.00, estimated_tip=3.00, 
         region="suburban", priority=4, is_depot=False),  # Lakeville
    
    # Western/Southwest Cities  
    Node(17, -8.0, -10.0, delivery_fee=11.30, estimated_tip=2.80, 
         region="suburban", priority=3, is_depot=False),  # Shakopee
    Node(18, -6.0, -12.0, delivery_fee=12.60, estimated_tip=2.70, 
         region="suburban", priority=4, is_depot=False),  # Prior Lake
    Node(19, -10.0, -9.0, delivery_fee=11.80, estimated_tip=2.90, 
         region="suburban", priority=4, is_depot=False),  # Chanhassen
    
    # Rural/Distant Cities
    Node(20, 18.0, -10.0, delivery_fee=15.00, estimated_tip=2.20, 
         region="rural", priority=4, is_depot=False),  # Hastings
    Node(21, 0.0, -20.0, delivery_fee=16.20, estimated_tip=2.40, 
         region="rural", priority=4, is_depot=False),  # Northfield
    Node(22, -5.0, -17.0, delivery_fee=14.90, estimated_tip=2.10, 
         region="rural", priority=4, is_depot=False),  # Lonsdale
    Node(23, -8.0, -18.0, delivery_fee=15.50, estimated_tip=2.00, 
         region="rural", priority=5, is_depot=False),  # New Prague
    Node(24, -15.0, 13.0, delivery_fee=16.80, estimated_tip=2.10, 
         region="rural", priority=4, is_depot=False),  # Monticello
]

# Find depot for easy access
MN_DEPOT = MN_NODES[0]  # Minneapolis is always node 0

# === Minnesota road edges ===================================
MN_EDGES = [
    # Major east-west spine (I-94 corridor)
    Edge(MN_NODES[24], MN_NODES[5]),   # Monticello - Maple Grove
    Edge(MN_NODES[5], MN_NODES[0]),    # Maple Grove - Minneapolis
    Edge(MN_NODES[0], MN_NODES[1]),    # Minneapolis - St Paul
    Edge(MN_NODES[1], MN_NODES[10]),   # St Paul - Woodbury
    Edge(MN_NODES[10], MN_NODES[9]),   # Woodbury - Stillwater
    
    # North arc (I-35 / 694 flavor)
    Edge(MN_NODES[5], MN_NODES[7]),    # Maple Grove - Anoka
    Edge(MN_NODES[7], MN_NODES[6]),    # Anoka - Blaine
    Edge(MN_NODES[6], MN_NODES[8]),    # Blaine - Forest Lake
    Edge(MN_NODES[8], MN_NODES[9]),    # Forest Lake - Stillwater
    
    # South/east arc (494/35E flavor)
    Edge(MN_NODES[1], MN_NODES[4]),    # St Paul - Roseville
    Edge(MN_NODES[1], MN_NODES[12]),   # St Paul - Eagan
    Edge(MN_NODES[12], MN_NODES[15]),  # Eagan - Rosemount
    Edge(MN_NODES[15], MN_NODES[14]),  # Rosemount - Apple Valley
    Edge(MN_NODES[14], MN_NODES[13]),  # Apple Valley - Burnsville
    Edge(MN_NODES[13], MN_NODES[16]),  # Burnsville - Lakeville
    Edge(MN_NODES[16], MN_NODES[21]),  # Lakeville - Northfield
    Edge(MN_NODES[21], MN_NODES[22]),  # Northfield - Lonsdale
    Edge(MN_NODES[22], MN_NODES[23]),  # Lonsdale - New Prague
    
    # Southwest arc (169 corridor)
    Edge(MN_NODES[2], MN_NODES[3]),    # Edina - Bloomington
    Edge(MN_NODES[3], MN_NODES[17]),   # Bloomington - Shakopee
    Edge(MN_NODES[17], MN_NODES[18]),  # Shakopee - Prior Lake
    Edge(MN_NODES[18], MN_NODES[19]),  # Prior Lake - Chanhassen
    Edge(MN_NODES[19], MN_NODES[5]),   # Chanhassen - Maple Grove
    
    # Downtown spokes
    Edge(MN_NODES[0], MN_NODES[2]),    # Minneapolis - Edina
    Edge(MN_NODES[0], MN_NODES[4]),    # Minneapolis - Roseville
    Edge(MN_NODES[0], MN_NODES[3]),    # Minneapolis - Bloomington
    Edge(MN_NODES[0], MN_NODES[5]),    # Minneapolis - Maple Grove
    Edge(MN_NODES[0], MN_NODES[12]),   # Minneapolis - Eagan
    
    # Additional connections for reachability
    Edge(MN_NODES[10], MN_NODES[11]),  # Woodbury - Cottage Grove
    Edge(MN_NODES[11], MN_NODES[20]),  # Cottage Grove - Hastings
    Edge(MN_NODES[4], MN_NODES[6]),    # Roseville - Blaine
    Edge(MN_NODES[2], MN_NODES[19]),   # Edina - Chanhassen
]