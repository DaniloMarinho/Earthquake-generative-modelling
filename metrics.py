import numpy as np
from scipy.spatial import distance
import ot
import pandas as pd


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

def earthquake_simulation_metric(samples):
    test_data = pd.read_csv('test_data.csv', index_col=0)
    test_samples = test_data[["Time", "Magnitude"]]
    test_samples["Time"] = test_samples["Time"] - test_samples["Time"].min()
    test_samples = test_samples.to_numpy()

    #Compute the Anderson Darling metric between the generated magnitudes and the true magnitudes
    AD_magnitudes = anderson_darling_distance(samples[:,1].reshape(-1,1), test_samples[:,1].reshape(-1,1)) 

    #Compute the W2 distance measuring the quality of the replication of the self-exciting behavior
    samples_v_i_list = [[samples[i+1][0]-samples[i][0], samples[i][1], 
                         samples[i+2][0]-samples[i+1][0], samples[i+1][1],
                         samples[i+3][0]-samples[i+2][0], samples[i+2][1],
                         samples[i+4][0]-samples[i+3][0], samples[i+3][1],
                         samples[i+5][0]-samples[i+4][0], samples[i+4][1],
                        ] for i in range(len(samples) - 5)]
    
    train_v_i_list = [[test_samples[i+1][0]-test_samples[i][0], test_samples[i][1], 
                       test_samples[i+2][0]-test_samples[i+1][0], test_samples[i+1][1],
                       test_samples[i+3][0]-test_samples[i+2][0], test_samples[i+2][1],
                       test_samples[i+4][0]-test_samples[i+3][0], test_samples[i+3][1],
                       test_samples[i+5][0]-test_samples[i+4][0], test_samples[i+4][1],
                      ] for i in range(len(samples) - 5)]
    
    vi_W2 = multivariate_wasserstein_distance(samples_v_i_list, train_v_i_list)
    return AD_magnitudes, vi_W2, AD_magnitudes+vi_W2