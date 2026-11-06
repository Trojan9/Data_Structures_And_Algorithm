#so here we are gonna use double linked list with a map..so this map will point to this
#so we would have two nodes left and right..all new needed nodes will be in between this two..so we will fix all coming key,val node in between

#so the idea is to have  two dummy nodes named left and right..so the most recently used node at the rightmost before the right node..so we just do self.right.prev and the least used at the leftmost side after left node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        #initialize prev and next to none..anythime we create a new node the prev and next is immediately none..by doing this we fit attach something to both side
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        #so this will hold our capacity which we will use to check if length of cache Map has exceeded this value
        self.cap = capacity
        self.cache = {}
        
        #so create our two node..which will be dummy nodes
        
        
        self.left, self.right = Node(0, 0), Node(0,0)
        
        #don't forget its a double linked list
        self.left.next = self.right
        self.right.prev = self.left
        
        
        
    def remove(self,node):
        #we get the prev and next of this node
        prev,nxt=node.prev,node.next
        #then sideline this node
        prev.next=nxt
        nxt.prev=prev
    def insert(self,node):
        #we insert at rightmost before the "right" dummy node
        #so we get the prev of the right dummy node
        prev,nxt=self.right.prev,self.right
        prev.next,nxt.prev=node,node
        
        node.prev,node.next=prev,nxt
    
    
    def get(self, key: int) -> int:
        if key in self.cache:
            #we also need to update the position of this node in the double linked list..so this node goes to the rightmost part before "right" dummy node, since its the most recently queried key..so we need two helper function to remove this node then insert at the rightmost before the "right" dummy node
            #remember the map returns a node for each key
            self.remove(self.cache[key])#remove
            self.insert(self.cache[key])#add to right
            return self.cache[key].val #since we are usig a node
        #otherwise return -1
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #we need to remove this node from linked list first...because we need to insert to right side...so we need to insert even if key is not there...so if key is there it would be a duplicate...so we first remove this key
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) #so we create the node in the map first
        self.insert(self.cache[key])#this map returns the node which is added to linked list
        
        #now we need to check if length of map keys is greater than the capacity we were given
        
        if len(self.cache) > self.cap:
            #we need to remove the leftmost node after the "left" dummy node
            #LRU..Least Recently Used
            
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
            #we justremove this node
            #remember we have the key and value stored in this lru node also
            
            
####### my preferred solution ###########################

from collections import OrderedDict
#an OrderedDict is a special kind of dictionary in Python that:
#Remembers the order in which you insert items.
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.orderDict:
            return -1
        #if yes..move key to last(lastest) since it was recently accessed
        self.orderDict.move_to_end(key)
        return self.orderDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderDict:
            #replace value and move to the end, as it is newly accessed
            self.orderDict[key] = value
            self.orderDict.move_to_end(key)
        else:
            self.orderDict[key] = value
            #pop the first item on the list, since that is the oldest in list
            #last is the lastest accesses
            if len(self.orderDict) > self.capacity:
                self.orderDict.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #32: LRU Cache (Medium)  [Linked List]
#
from collections import OrderedDict

# Brief: Fixed-capacity cache, O(1) get/put, evict least recently used when full.
#
# In plain words: a cache holding a fixed number of items that throws out the least recently used
# when full. You need two fast things: look up a key, and know which key is stalest. Python's
# `OrderedDict` is a dict that remembers order, treat the front as oldest and the back as newest.
# Every access moves the key to the back; when over capacity, drop the front.
#
# Why it works: `move_to_end` keeps the order meaning exactly "least → most recently used", so the
# stalest item is always the front, making eviction O(1).
#
# Algorithm
# 1. get: present → move to end, return; else -1. 2. put: set, move to end. 3. Over capacity → pop
#    front.

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()           # front = least recent, back = most recent
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)   # evict least recently used

# Complexity: Time O(1) per op, Space O(capacity).
