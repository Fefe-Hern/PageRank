import numpy as np
from page_rank import get_page_ranks, create_adjacency_matrix

if __name__ == '__main__':
    ""
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

    # get eigenvector of Adj Matrix
    M = create_adjacency_matrix(Adj)
    
    # get principal eigenvector of M
    eigenvalues, eigenvectors = np.linalg.eig(M)

    # find the index of the largest eigenvalue
    largest_eigenvalue_index = np.argmax(eigenvalues)
    principal_eigenvector = eigenvectors[:, largest_eigenvalue_index]

    print("ranks: ", ranks)
    print("principal eigenvector: ", principal_eigenvector)



