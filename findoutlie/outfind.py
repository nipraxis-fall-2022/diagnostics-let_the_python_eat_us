""" Module with routines for finding outliers
"""

from pathlib import Path

import numpy as np

import nibabel as nib

from .metrics import dvars, dvars_all
from .detectors import iqr_detector, iqr_detector_for_dvars_all
from .mahal import mahal


def detect_outliers(fname, method):
    """ Detect outliers given image file path `filename`
    Parameters
    ----------
    fname : str or Path
        Filename of 4D image, as string or Path object
    Returns
    -------
    outliers : array
        Indices of outlier volumes.
    """
    img = nib.load(fname)
    if method == dvars:
        is_outlier = iqr_detector(dvars(img), iqr_proportion=2)
    elif method == dvars_all: #note this is the gernalised dvars
        is_outlier = iqr_detector_uper_only(dvars_all(img, iqr_proportion=2)) # this will pickout anything 2 IQR over the 3rd Quantile
    else:                                                                         # note we are not doing under the 1st becasue dvars/dvars_all()
        is_outlier = iqr_detector_uper_only(mahal(img), iqr_proportion=2)                   # give an index of how much the volume deviates from something else
    # Return indices of True values from Boolean array.
    return np.nonzero(is_outlier)


def find_outliers(data_directory, method):
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
        if method == dvars:
            outliers = detect_outliers(fname, dvars)
            outlier_dict[fname] = outliers
        elif method == dvars_all:
            outliers = detect_outliers(fname, dvars_all)
            outlier_dict[fname] = outliers
        else:
            outliers = detect_outliers(fname, mahal)
            outlier_dict[fname] = outliers
    return outlier_dict