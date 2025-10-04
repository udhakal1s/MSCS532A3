# Umesh Dhakal
# MSCS532A3
# Hashing with Chaining

class HashingWithChaining:
    def __init__(self):
        self.tablesize = 20
        self.table = [[] for _ in range(self.tablesize)]

    def hash_func(self, key):
        return key % self.tablesize

    # add element in the list
    def insertitem(self, key, value):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    # search element from the list
    def searchitem(self, key):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    # delete element from the list
    def deleteitem(self, key):
        index = self.hash_func(key)
        for a, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][a]
                return True
        return False



if __name__ == "__main__":
    hashTable = HashingWithChaining()

    # Inserting elements
    hashTable.insertitem(25, "umesh") 
    hashTable.insertitem(26, "david")
    hashTable.insertitem(45, "sam")

    # Searching elements
    print("Search umesh:", hashTable.searchitem(25))
    print("Search david:", hashTable.searchitem(26))
    print("Search sam:", hashTable.searchitem(45))

    # Deleteing element
    hashTable.deleteitem(45)
    print("Search sam after delete:", hashTable.searchitem(45))