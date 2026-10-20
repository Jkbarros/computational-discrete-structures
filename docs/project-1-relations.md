# Project 1 — Binary relation properties

**Author:** Julio Barros  
**Source:** `Project 1/Project 1/Relation.java`

Reads a **10×10** matrix of `0`/`1` from a text file and reports whether the relation is:

| Property | Definition (matrix view) |
|----------|-------------------------|
| **Reflexive** | `mat[i][i] == 1` for all `i` |
| **Anti-reflexive** | `mat[i][i] == 0` for all `i` |
| **Symmetric** | `mat[i][j] == mat[j][i]` for `i ≠ j` |
| **Antisymmetric** | for `i ≠ j`, not both `mat[i][j]` and `mat[j][i]` equal 1 |

## Input format

Each line has ten integers separated by spaces, for example:

```text
1 0 1 0 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0
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

## Implementation notes

- File name is read from stdin; parsing uses `Integer.parseInt` on each token.
- Matrix size is fixed at 10 in this assignment build.
