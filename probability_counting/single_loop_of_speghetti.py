'''
You have a plate of spaghetti in front of you (no sauce!). You pick two ends and tie them together. Then you pick two more ends and tie them together. Continue until there are no free ends left. If there were n spaghettis originally, what is the probability that you now have a single giant loop consisting of all the spaghettis?

The theoretical probability can be derived as follows:
    fix one end of the 2*n ends.  This leaves 2n-1 possible ends to connect to.
    hence the probability of not connecting same piece is (2n-2)/(2n-1)
    this can be repeated to form numerator sequence of even numbers, and denominator dequence of odd numbers
    (2n-2)*(2n-4)..(2)/(2n-1)*(2n-3)...*(1)
    And this reduces to: get_theoretical_prob(n)

    The simulation first connects endpoints in the same piece and then proceeds to shuffle the ends and connect them randomly.

'''

import random
import scipy
import math
from collections import defaultdict

def get_probability_single_loop(trials, num_spaghetti):
    random.seed(10)
    n_left = num_spaghetti
    single_loop_count = 0
    for _ in range(trials):
        is_single_loop = simulate_spaghetti_pairing(n_left)
        single_loop_count += float(is_single_loop)

    return single_loop_count/trials
def is_cyclic_util(v, adj, visited, parent):
  
    # Mark the current node as visited
    visited[v] = True

    # Recur for all the vertices
    # adjacent to this vertex
    for i in adj[v]:
      
        # If an adjacent vertex is not visited,
        # then recur for that adjacent
        if not visited[i]:
            if is_cyclic_util(i, adj, visited, v):
                return True
              
        # If an adjacent vertex is visited and
        # is not parent of current vertex,
        # then there exists a cycle in the graph.
        elif i != parent:
            return True

    return False

def is_cyclic(u, adj, visited):
  
    # Call the recursive helper function
    # to detect cycle in different DFS trees
    # Don't recur for u if it is already visited
    if not visited[u]:
        if is_cyclic_util(u, adj, visited, -1):
            return True

    return False

def simulate_spaghetti_pairing(n):
    # Create a list of 2n ends (represented by numbers from 0 to 2n-1)
    ends = list(range(2 * n))
    
    # Randomly shuffle the ends
    random.shuffle(ends)
    
    # Pair the ends
    pairs = [(ends[2*i], ends[2*i+1]) for i in range(n)]
    mapping = defaultdict(list)
    #Connect original label i.e. 0-1, 1-2, ...
    for i in range(n):
        mapping[2*i].append(2*i+1)
        mapping[2*i+1].append(2*i)
    #print('pairs')
    #print(pairs) 
    # Create a mapping of which end connects to which other end
    for a, b in pairs:
        mapping[a].append(b)
        mapping[b].append(a)
    #print('mappings')
    #print(*mapping.items(), sep='\n') 
    # Now, check how many loops we have
    visited = [False] * (2 * n)
    loops = 0
    
    for i in range(2 * n):
        if not visited[i]:
            # Start a new loop
            if mapping[i][0]==mapping[i][1]:
                visited[i] = True
                visited[mapping[i][0]] = True
                loops += 1
            elif is_cyclic(i, mapping, visited):
                loops += 1
            
    #print('loops')
    #print(loops) 
    # If there's exactly 1 loop, return True (indicating a single giant loop)
    return loops == 1

def get_theoretical_prob(n):
    return (4**(n-1))*math.factorial(n-1)**2/math.factorial(2*n-1)

if __name__ == "__main__":
    for num_trials in [100000]:
        for num_spaghetti in [1, 2, 4, 10]:
            prob_single_loops = get_probability_single_loop(num_trials, num_spaghetti)
            theoretical_value = get_theoretical_prob(num_spaghetti)
            print(f"For {num_trials} trials and {num_spaghetti}, proportion with single loops is {prob_single_loops}")
            print(f"Versus Theoretical Probability: {theoretical_value}")
