""" Module with routines for finding outliers
"""

from pathlib import Path

import numpy as np

import nibabel as nib

from .metrics import dvars_all
from .spm_funcs import get_spm_globals
from .detectors import iqr_detector, iqr_detector_for_dvars_all


def detect_outliers(fname):
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
    dvars = dvars_all(img) #note this is the gernalised dvars
    is_outlier = iqr_detector_for_dvars_all(dvars, iqr_proportion=2) # this will pickout anything 2 IQR over the 3rd Quantile
                                                                     # note we are not doing under the 1st becasue dvars/dvars_all() 
                                                                     # give an index of how much the volume deviates from something else
    # Return indices of True values from Boolean array.
    return np.nonzero(is_outlier)


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
