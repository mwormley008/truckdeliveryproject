# class to create package objects
class Package:
    def __init__(self, package_id, del_address, del_city, del_state, del_zip, del_deadline, weight, special_notes):
        self.package_id = package_id
        self.del_address = del_address
        self.del_city = del_city
        self.del_state = del_state
        self.del_zip = del_zip
        self.del_deadline = del_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.departure_time = None
        self.delivered_time = None
        self.status = "Status: at hub"

    # F. Develop a look-up function that takes the following components as input and returns the
    # corresponding data elements:
    # package ID number, delivery address, delivery deadline, delivery city, delivery zip code,
    # package weight, delivery status (i.e., "at the hub", "en route", or "delivered"), including
    # delivery time
    # note: Your function should output all data elements for the package ID number.
    # O(1)
    def package_lookup(self, user_time):
        if user_time >= self.delivered_time:
            time = self.delivered_time
            status = "Status: delivered\n Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        return f"""Package ID: {self.package_id} \n 
                Address: {self.del_address} \n 
                City: {self.del_city} \n 
                State: {self.del_state} \n 
                Zip Code: {self.del_zip}\n 
                Deadline: {self.del_deadline} \n 
                Weight(kg): {self.weight} \n 
                Status: {status} \n Special Notes:{self.special_notes}"""