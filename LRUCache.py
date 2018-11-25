
import time

#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)

class Node:
    #Nodes - (n)=(n)=(n)=(n)
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    cache_limit = 3
    testing = 0 # If testing is set to 1, it will print the cache list of items etc so you can see the inner workings of program...
                # defaults to 0,

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def __call__(self, *args, **kwargs):
        #If in cache, pull results
        if args in self.cache:
            self.llist(args)
            if self.testing == 1:
                return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
            return self.cache[args]

        #If cache-limit reached - Remove LRU from node link list and dict - cache.
        if len(self.cache) > self.cache_limit:
            n = self.head.next
            self._remove(n)
            del self.cache[n.key]



        #Compute and cache and node - if not in cache
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        if self.testing == 1:
            return f'{result}\nCache: {self.cache}'
        return result

    #Remove from double linked-list - Node.
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
 
    #Add to double linked-list - Node.
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def llist(self, args):
        current = self.head
        while current != (0,0):
            if current.key == args :
                node = current
                self._remove(node)
                self._add(node)
                if self.testing == 1:
                    del self.cache[node.key]  # Debugging/ to view cache list in order of linked-list...
                    self.cache[node.key] = node.val # Debugging/ to view cache list in order of linked-list...
                break
            else:
                current = current.next


#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)
