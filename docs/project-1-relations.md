# Project 1 — Binary relation properties

**Author:** Julio Barros  
**Source:** [`Project 1/Project 1/Relation.java`](../Project%201/Project%201/Relation.java)  
**Sample input:** [`sample-relation.txt`](../Project%201/Project%201/sample-relation.txt)

Reads a **10×10** matrix of `0`/`1` from a text file and reports whether the relation is:

| Property | Definition (matrix view) |
|----------|-------------------------|
| **Reflexive** | `mat[i][i] == 1` for all `i` |
| **Anti-reflexive** | `mat[i][i] == 0` for all `i` |
| **Symmetric** | `mat[i][j] == mat[j][i]` for `i ≠ j` |
| **Antisymmetric** | for `i ≠ j`, not both `mat[i][j]` and `mat[j][i]` equal 1 |

> This submission checks the four properties above; **transitivity** is not implemented in `Relation.java`.

## Input format

Each line has ten integers separated by spaces:

```text
1 1 0 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
...
```

## Sample run

```text
File input: sample-relation.txt
Reflexive - yes
AntiReflexive - no
Symmetric - yes
Antisymmetric - no
```

## Core checks

```java
public static Boolean isReflexive(int mat[][] , int n) {
    for (int i = 0; i < n; i++)
        if (mat[i][i] != 1) return false;
    return true;
}

public static Boolean isSymmetric(int mat[][] , int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (i != j && mat[i][j] != mat[j][i]) return false;
    return true;
}
```

The program prompts for a filename on stdin, parses exactly ten rows, and prints `yes` / `no` for each property.
