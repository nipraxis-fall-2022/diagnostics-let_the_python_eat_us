""" Utilities for detecting outliers

These functions take a vector of values, and return a boolean vector of the
same length as the input, where True indicates the corresponding value is an
outlier.

The outlier detection routines will likely be adapted to the specific measure
that is being worked on.  So, some detector functions will work on values > 0,
other on normally distributed values etc.  The routines should check that their
requirements are met and raise an error otherwise.
"""

# Any imports you need
# +++your code here+++
from ast import Return
import numpy as np

def iqr_detector(measures, iqr_proportion=1.5):
    """ Detect outliers in `measures` using interquartile range.

    Returns a boolean vector of same length as `measures`, where True means the
    corresponding value in `measures` is an outlier.

    Call Q1, Q2 and Q3 the 25th, 50th and 75th percentiles of `measures`.

    The interquartile range (IQR) is Q3 - Q1.

    An outlier is any value in `measures` that is either:

    * > Q3 + IQR * `iqr_proportion` or
    * < Q1 - IQR * `iqr_proportion`.

    See: https://en.wikipedia.org/wiki/Interquartile_range

    Parameters
    ----------
    measures : 1D array
        Values for which we will detect outliers
    iqr_proportion : float, optional
        Scalar to multiply the IQR to form upper and lower threshold (see
        above).  Default is 1.5.

    Returns
    -------
    outlier_tf : 1D boolean array
        A boolean vector of same length as `measures`, where True means the
        corresponding value in `measures` is an outlier.
    """
    
    # Hints:
    # * investigate np.percentile
    # * You'll likely need np.logical_or
    # https://textbook.nipraxis.org/numpy_logical.html
    # +++your code here+++

    #Calculating the quartiels and the IQR for some vector called 'measures'
    Q1 = np.percentile(measures,25)
    Q3 = np.percentile(measures,75)
    IQR = Q3 - Q1
    outlier_tf = np.logical_or(measures < (Q1-(iqr_proportion * IQR)),measures > (Q3+(iqr_proportion * IQR)))
    return outlier_tf
    #we only want over if we use dvars

def iqr_detector_for_dvars_all(measures, iqr_proportion=1.5):
    """ Detect outliers in `measures` using interquartile range.

    Returns a boolean vector of same length as `measures`, where True means the
    corresponding value in `measures` is an outlier.

    Call Q1, Q2 and Q3 the 25th, 50th and 75th percentiles of `measures`.

    The interquartile range (IQR) is Q3 - Q1.

    An outlier is any value in `measures` that is either:

    * > Q3 + IQR * `iqr_proportion` or
    * < Q1 - IQR * `iqr_proportion`.

    See: https://en.wikipedia.org/wiki/Interquartile_range

    Parameters
    ----------
    measures : 1D array
        Values for which we will detect outliers
    iqr_proportion : float, optional
        Scalar to multiply the IQR to form upper and lower threshold (see
        above).  Default is 1.5.

    Returns
    -------
    outlier_tf : 1D boolean array
        A boolean vector of same length as `measures`, where True means the
        corresponding value in `measures` is an outlier.
    """
    
    # Hints:
    # * investigate np.percentile
    # * You'll likely need np.logical_or
    # https://textbook.nipraxis.org/numpy_logical.html
    # +++your code here+++

    #Calculating the quartiels and the IQR for some vector called 'measures'
    Q1 = np.percentile(measures,25)
    Q3 = np.percentile(measures,75)
    IQR = Q3 - Q1
    outlier_tf = (measures > (Q3+(iqr_proportion * IQR))) # Note Alex changed this to work with dvars_all() 
                                                          # becasue that code returns an index of difference 
                                                          # removing the lower tail doesnt make sense anymore
    return outlier_tf
    #we only want over if we use dvars