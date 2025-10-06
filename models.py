# models.py

class Place:
    def __init__(self, place_id, name, delivery_fee, tip_estimate):
        self.id = place_id
        self.name = name
        self.delivery_fee = float(delivery_fee)
        self.tip_estimate = float(tip_estimate)

    def __repr__(self):
        return f"Place({self.name}, fee={self.delivery_fee}, tip={self.tip_estimate})"


class Road:
    def __init__(self, from_id, to_id, travel_cost):
        self.from_id = from_id
        self.to_id = to_id
        self.travel_cost = float(travel_cost)

    def __repr__(self):
        return f"Road({self.from_id} -> {self.to_id}, cost={self.travel_cost})"
