import numpy as np
from page_rank import get_page_ranks, normalize_adjacency_matrix

if __name__ == '__main__':
    # Calling the page_rank function by itself will use the default values
    # The damping factor being at 1 will match the Eigenvector.

    # Create a random adjacency matrix for 7 sites.
    Adj = np.random.randint(2, size=(7, 7))
    


