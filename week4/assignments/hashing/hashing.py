class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
#        self.updatedslots = [None] * self.size
#        self.updateddata = [None] * self.size

    def hashfunction(self, key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self, key):
        # Insert your secondary hashing function code
        return key // self.size
    
    def put(self, key, data):
        # Insert your code here to store key and data 
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(key)
                if self.data[nextslot] == None:
                    self.data[nextslot] = data
                    self.slots[nextslot] = key

    def get(self, key):
        # Insert your code here to get data by key
        data = None
        position = self.hashfunction(key)
        if self.slots[position] == key:
            data = self.data[position]
        return data

    def __getitem__ (self, key):
        return self.get(key)

    def __setitem__ (self, key, data):
        self.put(key,data)

# Challenge: Create a new secondary hash function using your own algorithm that avoids all collisions with this data set
#    def newhashfunction(self, newkey):
#        return newkey % self.size

#    def updatedrehash(self, newkey):
#       return 7 * newkey % 11

#    def newput(self, newkey, updateddata):
#        newhashvalue = self.newhashfunction(newkey)
#        if self.updateddata[newhashvalue] == None:
#            self.updatedslots[newhashvalue] = newkey
#            self.updateddata[newhashvalue] = updateddata
#        else:
#            if self.updatedslots[newhashvalue] == newkey:
#                self.updateddata[newhashvalue] = updateddata
#            else:
#                updatednextslot = self.updatedrehash(newkey)
#                if self.updateddata[updatednextslot] == None:
#                    self.updateddata[updatednextslot] = updateddata
#                    self.updatedslots[updatednextslot] = newkey

#    def newget(self, newkey):
#        updateddata = None
#        updatedposition = self.newhashfunction(newkey)
#        if self.updatedslots[updatedposition] == newkey:
#            updateddata = self.updateddata[updatedposition]
#        return updateddata

#    def __getitem__ (self, newkey):
#        return self.newget(newkey)

#    def __setitem__ (self, newkey, updateddata):
#        self.newput(newkey, updateddata)

H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'
# Store remaining input data

# print the slot values
print("Slots: ", H.slots)

# print the data values
print("Data: ", H.data)

# print the value for key 52
print("Value for key 52: ", H[52])

# Output for challenge
# Create the updated hash table
#T = HashTable()
#T[69] = 'A'
#T[66] = 'B'
#T[80] = 'C'
#T[35] = 'D'
#T[18] = 'E'
#T[52] = 'F'
#T[89] = 'G'
#T[70] = 'H'
#T[12] = 'I'

# Store the original slot and data values for the updated table

# print updated Slots
#print('Updated Slots: ', T.updatedslots)

# print updated Data
#print('Updated Data: ', T.updateddata)

