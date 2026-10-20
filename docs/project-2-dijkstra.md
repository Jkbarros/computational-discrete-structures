# Project 2 — Dijkstra shortest paths

**Author:** Julio Barros  
**Source:** [`Project 2/Project 2/DijkstraExample.java`](../Project%202/Project%202/DijkstraExample.java)

Classic **Dijkstra** on an **adjacency matrix** with **9 vertices** (`totalVertex = 9`). Missing edges use weight **`-1`**; relax only when `graph[ux][vx] != -1`.

## Algorithm sketch

1. Initialize `distance[]` to ∞, `spSet[]` to false; `distance[source] = 0`.
2. Repeat `n - 1` times: pick unvisited `ux` with minimum distance, mark visited.
3. For each neighbor `vx`, if edge exists and path improves, update `distance[vx]`.
4. `printSolution` lists shortest distances from source **0**.

## Embedded graph (excerpt)

```java
int grph[][] = new int[][] {
    { -1, 3, -1, -1, -1, -1, -1, 7, -1 },
    { 3, -1, 7, -1, -1, -1, -1, 10, 4 },
    { -1, 7, -1, 6, -1, 2, -1, -1, 1 },
    // ... 9x9 total; see source file
};
obj.dijkstra(grph, 0);
```

## Sample output

```text
The shortest Distance from source 0th node to all other nodes are:
To 0 the shortest distance is: 0
To 1 the shortest distance is: 3
...
```

## Implementation note

`minimumDistance` scans all vertices each iteration (no priority queue). That matches the course emphasis on matrix representations for small dense graphs; for large sparse graphs you would use a heap and adjacency lists.
