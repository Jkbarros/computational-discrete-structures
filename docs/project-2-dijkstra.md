# Project 2 — Dijkstra shortest paths

**Author:** Julio Barros  
**Source:** `Project 2/Project 2/DijkstraExample.java`

Classic **Dijkstra** implementation on an **adjacency matrix** with **9 vertices**. Non-edges are encoded as `-1`; edge weights are positive integers.

## Algorithm sketch

1. Initialize distances to ∞, source distance `0`.
2. Repeat `n-1` times: pick the unvisited vertex with minimum distance, mark visited, relax neighbors.
3. Print shortest distances from source vertex `0`.

## Graph

The `main` method embeds a fixed 9×9 weight matrix (undirected-style weights on selected pairs). Running the program prints lines such as:

```text
The shortest Distance from source 0th node to all other nodes are:
To 0 the shortest distance is: 0
To 1 the shortest distance is: 3
...
```

## Why adjacency matrix here

The course emphasized matrix representations for small dense graphs. For sparse production graphs you would prefer adjacency lists and a priority queue — same algorithm, better scaling.
