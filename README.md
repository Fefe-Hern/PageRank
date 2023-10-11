# PageRank

Consider a small web, consisting of 6 pages: A, B, C, D, E, F  

- A links to B and C  
- B links to C and D  
- C links to A  
- D links to B and E  
- E links to B, D, and F  
- F links to E  

This can be visualized as an adjacency matrix.  
**Copilot: Create a Markdown-Formatted Adjacency matrix, M, based off what letter links to where.**

    A = |   | A | B | C | D | E | F |
        |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
        | A | 0 | 1 | 1 | 0 | 0 | 0 |
        | B | 0 | 0 | 1 | 1 | 0 | 0 |
        | C | 1 | 0 | 0 | 0 | 0 | 0 |
        | D | 0 | 1 | 0 | 0 | 1 | 0 |
        | E | 0 | 1 | 0 | 1 | 0 | 1 |
        | F | 0 | 0 | 0 | 0 | 1 | 0 |

## Initialization  

We can normalize the columns of A, so that each column sums to 1.  
Afterwards, we assign each page a rank of 1/6.  
**Note: We can calculate the rank of each page using:**  

    python:
    r = np.ones(M.shape[1]) / M.shape[1]

Within the function itself.
