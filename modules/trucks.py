class Truck:
    def __init__(self, packages, depart_time, truck_id):
        self.undelivered = packages
        self.depart_time = depart_time
        self.truck_id = truck_id
        self.capacity = 16
        self.speed = 18
        self.miles_traveled = float(0.0)
        self.delivered = []
        self.start_address = "4001 South 700 East"
        self.current_address = self.start_address
        self.current_time = None
        self.return_time = None