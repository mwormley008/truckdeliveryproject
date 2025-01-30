# class to create package objects
class Package:
    def __init__(self, package_id, del_address, del_city, del_state, del_zip, del_deadline, weight, special_notes):
        self.package_id = package_id
        self.del_address = del_address
        self.del_city = del_city
        self.del_state = del_state
        self.zip_code = del_zip
        self.deadline = del_deadline
        self.weight = weight
        self.notes = special_notes
        self.departure_time = None
        self.delivered_time = None
        self.status = "at hub"

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
            status = "Satus: delivered\t Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t Zip Code: %s" \
               "\t Deadline: %s \t Weight(kg): %s \t %s \t %s" % (
                self.package_id, self.del_address, self.del_city, self.del_state, self.zip_code,
                self.deadline, self.weight, status, self.notes)