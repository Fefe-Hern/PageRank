import numpy as np


def get_page_ranks(Adj, damping_factor):
    """
    Calculates the page ranks of a given adjacency matrix.

    Args:
        Adj (list): The adjacency matrix, which page links to which.
        damping_factor (float): The damping factor used in the PageRank algorithm.

    Returns:
        numpy.ndarray: The final page ranks of the nodes in the graph.
    """
    M = normalize_adjacency_matrix(Adj)
    final_ranks, iterations = __check_convergence(M, damping_factor)

    return final_ranks, iterations


def normalize_adjacency_matrix(Adj):
    """
    Creates a normalized adjacency matrix from a given adjacency matrix.

    Args:
        Adj (list): The adjacency matrix of the graph.

    Returns:
        numpy.ndarray: The normalized adjacency matrix of the graph.
    """
    A = np.array(Adj, dtype=float)
    # normalize the matrix by column
    col_sums = A.sum(axis=0)
    M = A / col_sums
    return M


def __update_ranks(M, r, orig, damp):
    """
    Updates the page ranks of the nodes in the graph using the PageRank algorithm.

    Returns:
        numpy.ndarray: The updated page ranks of the nodes in the graph.
    """
    return (damp * (M @ r)) + ((1-damp)*orig)


def __check_convergence(M, damping_factor):
    """
    Checks the convergence of the page ranks of the nodes in the graph

    Args:
        M (numpy.ndarray): The normalized adjacency matrix of the graph.
        damping_factor (float): The damping factor used in the PageRank algorithm.

    Returns:
        numpy.ndarray: The final page ranks of the nodes in the graph.
    """
    r = np.ones(M.shape[1]) / M.shape[1]
    orig = np.ones(M.shape[1]) / M.shape[1]
    iterations = 0
    flag = True

    while flag:
        iterations += 1
        new_r = __update_ranks(M, r, orig, damping_factor)
        if np.allclose(r, new_r, atol=1e-6):
            #print("Converged in {} iterations".format(iterations))
            flag = False
        else:
            r = new_r
    return r, iterations


# Main function in case you want to run this file
if __name__ == '__main__':
    # verifying correctness of the page rank algorithm
    damping_factor = 1
    Adj = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0]
        ]
    ranks, iterations = get_page_ranks(Adj, damping_factor)
    # Round to 2 decimal places:
    print("ranks: ", np.round(ranks, 2))

    # Verification phase:
    # get eigenvector of Adj Matrix
    M = normalize_adjacency_matrix(Adj)
    
    # get principal eigenvector of M
    eigenvalues, eigenvectors = np.linalg.eig(M)
    ## find the index of the largest eigenvalue
    largest_eigenvalue_index = np.argmax(eigenvalues)
    principal_eigenvector = eigenvectors[:, largest_eigenvalue_index]
    ## normalize the principal eigenvector
    principal_eigenvector = principal_eigenvector / np.sum(principal_eigenvector)

    # Only show the real eig values, not imaginary.
    print("principal eigenvector: ", principal_eigenvector.real)