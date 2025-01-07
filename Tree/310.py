# minimum height trees
"""
This question asks to return the minimum height tress
as the MHT's nature is only one/two nodes, so we can delete the out layer of nodes
till we find the root number is less than 2
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        # here we are initiating an adjacent lists
        neighbours = [set() for i in range(n)]
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        # we need to go through the graph, to get the most out layer of leaves,
        # which means its length is 1
        leaves = []
        for i in range(n):
            if len(neighbours[i]) == 1:
               leaves.append(i)
        # to check if we already remove all out layer leaves
        remain_node = n
        while remain_node > 2:
            remain_node -= len(leaves)

        # if there are remaining leaves,
        # here we are gonna keep removing the leaves form the graph
            new_leaves = []
            while leaves:
                # it indicates this leave could be removed, as it has no child
                # we pop it then also find it in graph to pop it,
                # and update the adjacent list
                to_remove_leaves = leaves.pop()
                neighbours = neighbours[to_remove_leaves].pop()
                neighbours[to_remove_leaves].remove(to_remove_leaves)
                # until we remove all the out layer leaves, and there is one node left
                # which means we find the last node, we can append it to the ans, here is leaves
                if len(neighbours[to_remove_leaves]) == 1:
                    new_leaves.append(to_remove_leaves)
            leaves = new_leaves

        return leaves
#time/ space O(|v|)