class ChainingHashTable:
    # HashTable class using chaining.
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10, load_factor_threshold=0.75):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        self.size = 0
        self.load_factor_threshold = load_factor_threshold
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts either a new item into or updates an item in the hash table.
    def insert(self, key, item):
        if self.size / len(self.table) > self.load_factor_threshold:
            self.resize()
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        self.size += 1
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                # if found return the key's value that is in the bucket list.
                # return after calling the getter function for the value in bucket list.
                return key_value[1]

        # the key is not found.
        return None
    
    def resize(self):
        # Create a new table with double the size
        new_capacity = len(self.table) * 2
        new_table = []
        
        for i in range(new_capacity):
            new_table.append([])
        
        # Rehash all existing items to the new table
        for bucket_list in self.table:
            for key_value in bucket_list:
                key, item = key_value
                new_bucket = hash(key) % new_capacity
                new_table[new_bucket].append([key, item])
        
        self.table = new_table
        # print(f"Resized table to new capacity: {new_capacity}")