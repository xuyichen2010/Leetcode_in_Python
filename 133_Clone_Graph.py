# https://leetcode.com/problems/clone-graph/solution/

# BFS
# O(N) Visiting each node exactly once
# O(N) Space is occupied by the visited

# Deep copy is a process in which the copying process occurs recursively.
# It means first constructing a new collection object and then recursively populating
# it with copies of the child objects found in the original. In case of deep copy,
# a copy of object is copied in other object.
# It means that any changes made to a copy of object do not reflect in the original object.

# A shallow copy means constructing a new collection object and then populating it
# with references to the child objects found in the original.
# The copying process does not recurse and therefore won’t create copies of the child
# objects themselves. In case of shallow copy, a reference of object is copied in other object.
# It means that any changes made to a copy of object do reflect in the original object.

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = self.get_all_nodes(node)
        old_to_new = {}

        for old_node in nodes:
            old_to_new[old_node] = Node(old_node.val, [])

        for old_node in nodes:
            for neighbor in old_node.neighbors:
                new_node = old_to_new[old_node]
                new_node.neighbors.append(old_to_new[neighbor])
        return old_to_new[node]

    def get_all_nodes(self, node):
        queue = deque()
        res = set()
        queue.append(node)
        res.add(node)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in res:
                    queue.append(neighbor)
                    res.add(neighbor)
        return res

# DFS
# O(n)
# O(n)
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node):

        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node