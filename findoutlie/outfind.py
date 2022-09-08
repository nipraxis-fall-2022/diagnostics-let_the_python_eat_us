""" Module with routines for finding outliers
"""

from pathlib import Path

import nibabel as nib

import numpy as np


def detect_outliers(fname):
    img = nib.load(fname)
    data = img.get_fdata()
    OneD_scans = data.reshape((-1, data.shape[-1])) #Alex: recall reshape((newshape),order)
                                                                # So this returns a 2D array  with
                                                                    # rows of length -1 (i.e. np solves it)
                                                                    # and columsn corriposnding to time stamps (scans) 
                                                                # Basically we gets each scan flattended to 1D
    means = np.mean(OneD_scans, axis=0)
    std_of_means = np.std(means)
    threshold = 2* std_of_means
    outliers = np.where(np.abs(means - np.mean(means)) > threshold)
    return outliers


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = Path(data_directory).glob('**/sub-*.nii.gz')
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
