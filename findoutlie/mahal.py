''' Mahalanobis distance 

Definition:
see https://www.sciencedirect.com/topics/engineering/mahalanobis-distance

"The Mahalanobis distance is a distance measure that takes into account the correlation in the data by using the precision matrix (inverse of the covariance matrix)"
--> In simpler terms: measures the distance between a point and a distribution.





For application to fmri data:
see https://arxiv.org/pdf/2101.04408.pdf

"The Mahalanobis distance calculates the Euclidean distance between each data point and the sample mean, and scales
it by the variance in the direction of the vector that joins the two points."




Formula:
see https://www.machinelearningplus.com/statistics/mahalanobis-distance/

  D^2 (x - m)T . C^-1. (x - 1)

 - D^2        is the square of the Mahalanobis distance.
 - x          is the vector of the observation (row in a dataset),
 - m          is the vector of mean values of independent variables (mean of each column),
 - C^(-1)     is the inverse covariance matrix of independent variables.




'''

import numpy as np


def mahal(img):
    img_data = img.get_fdata()
    data_reshaped = np.reshape(img_data, (-1, img_data.shape[-1]))
    # Excluding data based on spm global
    mean_vol = np.mean(data_reshaped, axis=-1)
    mean_mean = np.mean(mean_vol)
    thresh = mean_mean / 8  # the "spm global" function
    mask = mean_vol > thresh
    data = data_reshaped[mask, :]  # keeping only voxels above threshold
    mahal_dist_lst = []
    for vol_no in range(data.shape[-1]):
        this_vol = data[:, vol_no]
        # covariance of volume
        cov = np.cov(this_vol.T)
        # np.cov is based on the np.dot product (i.e. sum of vector multiplication)
        # but be careful because np.dot is missing the / N-1 normalization
        # so np.cov differs from np.dot(this_vol.T, this_vol.conj()) or even np.sum(this_vol*this_vol)
        # see https://stackoverflow.com/questions/21759026/python-covariance-matrix-by-hand
        # https://stackoverflow.com/questions/50879686/different-results-for-covariance-matrix-when-using-numpy-cov
        # next, we take away the mean of volume data from current volume
        this_vol_minus_mean = this_vol - np.mean(data, axis=1)
        # now we calculate the inverse of covariance
        # so we try this: https://stackoverflow.com/questions/58085632/how-to-calculate-mahalanobis-distance-between-randomly-generated-values
        # but np.linalg.inv() doesn't work because cov looks like an empty array, test with: print(cov.shape, type(cov))
        # so because of that we get numpy.linalg.LinAlgError: 0-dimensional array given.
        # so instead we try this: https://stackoverflow.com/questions/52289379/invert-singular-matrix-on-python
        # but covariance^-1 throws a ufunc 'bitwise_xor'  error
        # so instead we try this: see here https://docs.python.org/3.6/library/functions.html#pow
        # but now the operand @  throws error (dimensions error), see here: https://stackoverflow.com/questions/34142485/difference-between-numpy-dot-and-python-3-5-matrix-multiplication
        # so going for .dot
        mahal_distances = (np.sqrt(this_vol_minus_mean.T.dot(pow(cov, -1)).dot(this_vol_minus_mean)))
        mahal_dist_lst.append(mahal_distances)
    return np.array(mahal_dist_lst)
