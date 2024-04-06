from collections import deque
import heapq

# Arrays
arr = [1, 2, 3, 4, 5]

# Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Stacks
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_element = stack.pop()

# Queues
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
dequeued_element = queue.popleft()

# Trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Graphs
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Hash Tables
hash_table = {}
hash_table['key1'] = 'value1'
value = hash_table.get('key1')

# Heaps
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
min_value = heapq.heappop(heap)

# Tries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

# Sets
my_set = {1, 2, 3, 4, 5}

# Maps (Dictionaries)
my_map = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Displaying data structures
print("Array:", arr)
print("Linked List:")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
current = ll.head
while current:
    print(current.data, end=" ")
    current = current.next
print("\nStack:", stack)
print("Queue:", list(queue))
print("Binary Tree: root ->", root.value)
print("Graph:", graph)
print("Hash Table:", hash_table)
print("Heap:", heap)
print("Trie (just structure):", Trie().__dict__)
print("Set:", my_set)
print("Map:", my_map)
