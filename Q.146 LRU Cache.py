class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value 
        
# Yesterday I solved problem 146 (LRU Cache). So far, I have solved 88 problems on leetcode. I didn't post this problem yesterday because I didn't feel I fully understood part of the solution and wanted to have a night to sink the solution in my mind. Now I feel I am confident to post my solution as well as the explanation here.

# A computer has its own capacity limit to store some 'floating' data' that helps to retrieve an app quickly instead of reopening it from zero, so every time when we first interact with an app, it starts 'floating' in the memory; when we first open another app, it also starts 'floating' in the memory but stays in front of the first app that was opened. At some point, those 'floating' apps may exceed the limit of the capacity, in which case requires us to remove the least used (which stays at the bottom in the memory) apps.

# There are three important details that we need to carefully consider while writing such a program. 1) data structure that can help us to retrieve the 'floating' cache fast.. what is that? HashMap! 2) keep track of the used capacity.. which can be implied by the size of the hashmap. 3) keep track of the cache.. we want to move any most lately interacted 'floating' cache to the front and update the cache if needed.. doubly linked list sounds like a good idea!

# Okay.. now we're ready to write the program.
# 1) Define a node class of DLL that contains key and value.
# 2) Define a head node, a tail node of DLL, a hashmap to store the node key and the node, and the initial capacity.
# 3) get(key) will return the value of the node. We first need to check if the key is contained in the map. If yes, get the value, and very importantly, remove the node from DLL and insert the node to the front of DLL because we just interacted with it by getting its value! If no, return -1.
# 4)put(key, value) will put a new node to the cache. We need to first put it into the map. If the map contains the key, update the value and again, remove the node and put it to the front of the DLL. If not and exceeds the capacity limit, remove the last node from the map and from the DLL and insert the node to the front of the DLL.
# 5) insert(node) handles inserting a node to the front of the DLL and insert it to the map.
# 6) remove(node) handles removing a node from the DLL.

# The time complexity is O(1) and space complexity is O(capacity).
