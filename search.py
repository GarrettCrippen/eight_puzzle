from queue import PriorityQueue
def uniform_cost_search(root): 
    q= PriorityQueue() 
    visited = set()
    visited.add(root)
    for children in root:
