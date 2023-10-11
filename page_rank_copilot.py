import numpy as np

# Copilot code has been preserved in the areas where they were used. Denoted with ##
# Copilot Code was cleaned up. It used a Depreciated function np.matrix instead of np.array
# All methods made public for testing.
# For cleaned up version of the code, please check page_rank.py

def get_page_ranks(Adj, damping_factor):
    M = create_adjacency_matrix(Adj)
    final_ranks = check_convergence(M, damping_factor)

    return final_ranks


def create_adjacency_matrix(Adj):
    A = np.array(Adj, dtype=float)
    ## Create a matrix M which is the column-normalized version of A
    ## use numpy to create a matrix M
    # normalize the matrix by column
    col_sums = A.sum(axis=0)
    M = A / col_sums
    return M

## Create a function that updates each entry in r, the page rank, using the following formula
## r = damping_factor*M*r + (1-damping_factor)*original
def update_ranks(M, r, orig, damp):
    return damp * (M @ r) + (1-damp)*orig

## Create a function that checks if the page rank has converged
## if the page rank has converged, print the number of iterations it took to converge
## if the page rank has not converged, update the page rank and repeat

def check_convergence(M, damping_factor):
    r = np.ones(M.shape[1]) / M.shape[1]
    orig = np.ones(M.shape[1]) / M.shape[1]
    iterations = 0
    flag = True

    while flag:
        iterations += 1
        new_r = update_ranks(M, r, orig, damping_factor)
        if np.allclose(r, new_r):
            print("Converged in {} iterations".format(iterations))
            flag = False
        else:
            r = new_r
    return r

# Main function in case you want to run this file
""" ##
Consider a small web, consisting of 6 pages: A, B, C, D, E, F

A links to B and C, B links to C and D, C links to A
D links to B and E, E links to B, D, and F, F links to E

Create an adjacency matrix A 
"""
if __name__ == '__main__':
    damping_factor = 0.85
    Adj = [[0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0]]
    get_page_ranks(Adj, damping_factor)