# -*- coding: utf-8 -*-
#
#    Copyright (C) 2018 by
#    Thomas Bonald <thomas.bonald@telecom-paristech.fr>
#    All rights reserved
#    BSD license

import numpy as np
from scipy import sparse as sp

## Spectral embedding

def spectral_embedding(adjacency, embedding_dimension = 100, weights = None):
    """Spectral embedding 

     Parameters
     ----------
     adjacency : scipy sparse matrix
         Adjacency matrix of an undirected, weighted, connected graph
     embedding_dimension : int, optional
         Dimension of the embedding space (default value = 100)
     weights : array_like, optional 
         Node weights, all positive (default value = 1)
         

     Returns
     -------
    eigen_val : numpy array
         1D array
         Eigenvalues
    eigen_vec : numpy array
         2D array
         Eigenvectors
    embedding : numpy array
         2D array
         Embedding of the graph
    """

    # Weighted Laplacian
    n = np.shape(adjacency)[0]
    degrees = sp.csr_matrix.dot(adjacency, np.ones(n))
    degrees_diag = sp.diags(degrees)
    laplacian = degrees_diag - adjacency   
    if weights == None:
        weights = np.ones(n)
    sqrt_inv_weights_diag = sp.diags(1 / np.sqrt(weights))
    weighted_laplacian = sqrt_inv_weights_diag.dot(laplacian.dot(sqrt_inv_weights_diag))

    # Spectral decomposition
    eigen_val, eigen_vec = sp.linalg.eigsh(weighted_laplacian, min(embedding_dimension + 1, n - 1), which='SM')

    # Normalization
    sqrt_inv_eigen_val_diag = sp.diags(1 / np.sqrt(eigen_val[1:]))
    embedding = sqrt_inv_eigen_val_diag.dot(sqrt_inv_weights_diag.dot(eigen_vec[:,1:]).T)

    return eigen_val,eigen_vec,embedding
