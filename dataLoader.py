# Starter code. 
# Handles CSV file reading and builds adjacency lists. 
import csv
from models import Place, Road

def load_destinations(filename):
    """Load delivery destinations (nodes)."""
    destinations = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            place = Place(row['id'], row['name'], row['delivery_fee'], row['tip_estimate'])
            destinations[place.id] = place
    return destinations


def load_roads(filename):
    """Load roads (edges) and build adjacency list."""
    roads = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            a, b, cost = row['from_id'], row['to_id'], float(row['travel_cost'])
            roads.setdefault(a, []).append((b, cost))
            roads.setdefault(b, []).append((a, cost))  # assume undirected
    return roads
