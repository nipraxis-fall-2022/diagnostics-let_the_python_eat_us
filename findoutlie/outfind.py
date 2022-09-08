""" Module with routines for finding outliers
"""

from pathlib import Path

import nibabel as nib

import numpy as np

from findoutlie import spm_funcs as spm # call our spm_funcs .py file (given to us - unchanged)

from findoutlie import detectors as det # calls our detectors .py file (which we wrote)


def detect_outliers(fname):
    data_inside = spm.get_spm_globals(fname) #Alex: Before we look for outliers lets figure out whats in the head
                                                        # This applies the SPM method to the file 
                                                        # and returns a mean per volume.
    outliers_tf = det.iqr_detector(data_inside,1.5) # Alex: this takes those means and applies the Tukey method (IQR)
                                                        # The function then returns True if the volume is an outlier
    outliers = np.where(outliers_tf==True) # Alex: This then returns a set of indecies corrisponding to the outliers
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
