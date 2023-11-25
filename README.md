# Min-Chain-Partitioning

### Summary
 One of two practical assignments for the course Algorithms and Datastructures. A variant of the box-stacking problem is given, which essentially comes down to a minimum chain partitioning (also called Dilworth partitioning) problem. This problem can be reformulated as a bipartite matching problem, which is efficiently solved in O(n^2.5) time where n is the size of the poset. 
 
### Implementation

The implementation of Hopcroft-Karp presented here is different from Wikipedia, and faster. There is no distance dictionary for keeping track of the layers. Rather, a BFS lattice is built every BFS iteration, which is then explored backwards in the DFS phase. Nodes are marked as visited, but edges are not: rather, we use a residual graph (like in the Ford-Fulkerson algorithm) to keep track of the direction in which edges may be traversed. This was apparently an approach that Python could execute much faster, because only this approach was what made us pass all the test cases without time limits!

### Contents

The repo contains the code, and a report. 

- The report features a proof of correctness and complexity analysis. 
- The code is split up into 2 classes and a main program: 
  1. class Matching (`bipartiteMatching.py`) for solving general bipartite matching problems using Hopcroft-Karp.
  2. class MinChainPartition (`minChainPartition.py`) for solving general minimum-chain partitioning problems. It is backed by the class Matching, of course.
  3. a main program (`main.py`) which contains code specific to solving the box-fitting problem specified in the problem statement. It contains relevant functions to this problem, such as the relation defining the partial order on the boxes, and a function for getting and parsing the specified input format.

### Usage

If you want to use the code to solve your own box stacking problem, please read the problem statement to see the required input format. The `main.py` script will wait for input in the specified format and print a minimum number of chains to stdout.

I included one large and one small test case that you can copy-paste into the terminal, along with the expected output. Try this if you are interested, or if you cannot come up with interesting test cases of 5000 boxes yourself.

It should be noted that the I/O part of the program is mainly constructed for testing purposes in an automated testing environment (DOMJudge). The classes are however implemented for general min-chain partitioning problems or bipartite matchings and can certainly be reused in many different scenarios.


