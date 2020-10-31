''' Problem Description

Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node
B[i][0] to node B[i][1].
Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.

Approach : Create a queue and a visited array initially filled with 0, of size V where V is number of vertices.
Insert the starting node in the queue, i.e. push u in the queue and mark u as visited.
Run a loop until the queue is not empty.
Dequeue the front element of the queue. Iterate all its adjacent elements. If any of the adjacent element is the destination return 1. Push all the adjacent and unvisted vertices in the queue and mark them as visited.
Return 0 as the destination is not reached in BFS.

Complexity : Time Complexity: O(A + M) where A is number of vertices in the graph and M is number of edges in the graph.
Space Compelxity: O(A)'''

rom collections import defaultdict

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, t, E):
        es = defaultdict(list)
        
        for e in E:
            es[e[0]].append(e[1])
        
        stack = [1]
        visited = set([1])
        while stack:
            u = stack.pop()
            for v in es[u]:
                if not v in visited:
                    stack.append(v)
                    visited.add(v)
                    
        return 1 if t in visited else 0



