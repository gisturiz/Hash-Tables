# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        # hash the key
        key_hash = self._hash_mod(key)

        # create link pair node variable
        new_node = LinkedPair(key, value)

        # if storage at index is None, insert key, value at index
        if self.storage[key_hash] is None:
            self.storage[key_hash] = new_node
        # elif if key already exist, update value
        elif self.storage[key_hash].key == key:
            self.storage[key_hash].value = value
        else:
            # go to index on storage
            last_item = self.storage[key_hash]
            # walk through LL and check for the last item or key match
            while last_item.next is not None and last_item.key != key:
                last_item = last_item.next
            # if key matches, update value
            if last_item.key == key:
                last_item.value = value
            # otherwise, create new node at end of LL
            last_item.next = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''

        # hash index key
        key_hash = self._hash_mod(key)
        item = self.storage[key_hash]

        # if index not empty
        if item is not None:
            # and key matches
            if item.key == key:
                # assign the value to None
                item.value = None
            else:
                cur_item = item.next
                while cur_item is not None:
                    if cur_item.key == key:
                        cur_item.value = None
                    cur_item = cur_item.next
        # or if not found
        else:
            print("Key not found!")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        # hash the key
        key_hash = self._hash_mod(key)
        item = self.storage[key_hash]

        # if index is not empty
        if item is not None:
            # and key matches
            if item.key == key:
                # return key value
                return item.value
            else:
                cur_item = item.next
                while cur_item is not None:
                    if cur_item.key == key:
                        return cur_item.value
                    cur_item = cur_item.next
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''

        # save current storage to temp variable
        old_storage = self.storage
        # increase capacity by multiple of 2
        self.capacity *= 2
        # set storage to an empty list
        self.storage = [None] * self.capacity

        # insert each item in old storage which is not none
        for item in old_storage:
            # if the head is the only item, insert just that
            if item is not None and item.next is None:
                self.insert(item.key, item.value)
            # if there is a LL, iterate over list and insert each one
            if item is not None and item.next is not None:
                cur_item = item
                while cur_item.next is not None:
                    self.insert(cur_item.key, cur_item.value)
                    cur_item = cur_item.next
                # insert the last node in LL
                self.insert(cur_item.key, cur_item.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
