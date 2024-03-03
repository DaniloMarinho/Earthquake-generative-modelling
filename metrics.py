import numpy as np
from scipy.spatial import distance
import ot


def anderson_darling_distance(data_og, data_gen):
    data_og = np.array(data_og)
    data_gen = np.array(data_gen)
    n = data_og.shape[0]
    d = data_og.shape[1]

    assert data_og.shape == data_gen.shape, "Data sets must have the same shape"

    u_tilde = np.array([mod_prob(data_og[:, i], data_gen[:, i], n) for i in range(d)])

    weigth = np.array([(2*i + 1) for i in range(n)])
    W = - n - np.mean((weigth * (np.log(u_tilde) + np.log(1 - u_tilde[:, :: -1]))), axis=1)

    return np.mean(W)


def mod_prob(v_og, v_gen, n):
    v_gen = np.sort(v_gen)
    u_tilde = np.array([sum(v_og <= v_gen[i]) for i in range(n)])
    return (u_tilde + 1)/(n+2)


def euclidean_distance_matrix(x, y):
    return distance.cdist(x, y)


# empiprical distributions assume uniform weights
def multivariate_wasserstein_distance(x, y):
    assert len(x) == len(y), "Data sets must have the same shape"
    n = len(x)
    M = euclidean_distance_matrix(x, y)
    p = np.ones(n) / n
    q = np.ones(n) / n
    return ot.emd2(p, q, M)
