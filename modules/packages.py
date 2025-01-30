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
        self.status = "Status: At hub"

    #B. Develop a look-up function that takes the package ID as input and returns the attributes of the package
    def package_lookup(self, input_time):
        # Delivery status
        if input_time >= self.delivered_time:
            time = self.delivered_time
            status = f"Status: Delivered (at {str(time)})" 
        elif self.delivered_time > input_time > self.departure_time:
            status = "Status: En route"
        else:
            status = "Status: At hub"

        return f"""Package ID: {self.package_id}
                Address: {self.del_address}
                City: {self.del_city}
                State: {self.del_state}
                Zip Code: {self.del_zip}
                Deadline: {self.del_deadline}
                Weight(kg): {self.weight}
                {status} \n Special Notes:{self.special_notes}"""