#Linear Probing - Associative Arrays Implementation 

class HashTable:

    def __init__(self):
        
        self.capacity = 10
        self.keys = [None]*self.capacity
        self.values = [None]*self.capacity

    # Hash function to decide the placement of every item in the array
    def hash_function(self, key):

        hash_sum = 0

        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity

    # Function to insert an item into the array
    def insert(self, key, data):

        index = self.hash_function(key)
        
        while self.keys[index] is not None:

            if self.keys[index] == key:
                self.values[index] = data
                return

            index = (index + 1) % self.capacity

        self.keys[index] = key
        self.values[index] = data

    # Function to return the data stored given the key
    def get(self, key):

        index = self.hash_function(key)

        while self.keys[index] is not None:
            
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        return None


# Testing
if __name__ == '__main__':

    table = HashTable()
    table.insert('adam',23)
    table.insert('kevin',45)
    table.insert('Daniel',34)
    print("adam:",table.get('adam'))
    print("test:",table.get('test'))
