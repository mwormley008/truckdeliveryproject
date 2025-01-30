from modules.import_csv import *
import datetime

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

    def show_packages_at_time(self, input_time):
        """
        Show which packages are on the truck at a given time.
        Will iterate through undelivered packages and check if the current time matches the delivery time.
        """
        still_on_truck = []
        time = convert_time(input_time)
        for package_id in self.delivered:
            package = hash_table.search(package_id)
            # If the package should be delivered by the given time, print it
            # package_time = package.delivered_time
            if package.delivered_time:
                if package.delivered_time > time:
                    print(package.delivered_time)
                    still_on_truck.append(package.package_id)
        
        return still_on_truck
    

def convert_time(user_time):
    (h, m, s) = user_time.split(":")
    h = int(h)
    m = int(m)
    s = int(s)
    return datetime.timedelta(hours=h, minutes=m, seconds=s)