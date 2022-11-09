"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = []
        new_nodes = {}
        q = []
        if not node: return 
        print(node, q)
        q.append(node)
        copy = Node(node.val)
        new_nodes[node.val] = copy
        while q:
            curr = q.pop()
            copy = new_nodes[curr.val]
            for n in curr.neighbors:
                if not n.val in new_nodes:
                    new_node = Node(n.val)
                    new_nodes[n.val] = new_node
                copy.neighbors.append(new_nodes[n.val])
                if not n.val in visited:
                    q.append(n)
                    visited.append(n.val)
            visited.append(curr.val)
        return new_nodes[1]
            