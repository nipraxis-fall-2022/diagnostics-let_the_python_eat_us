""" Scan outlier metrics
"""

# Any imports you need
from operator import index
import numpy as np
from pathlib import Path


def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    data = img.get_fdata()
    n_voxels = np.prod(img.shape[:-1]) # Alex: this calcuates how many voxels are in a volume so we can 
                                            # calculate the mean voxel value later 
    lst = []
    for i in range(img.shape[-1]): #Alex: this gets a series of volumes along time (the last demenstion)
        if (data[..., i] == data[..., -1]).all(): # Alex: if the volume is the last in the series, 
                                                        # Why do we need .all()?
            #print(i, "last skipped!")   #just to check it's working
            continue # Alex: continue casues the loop to skip the rest of the loop and start the next iteration
        this_vol = data[..., i]
        next_vol = data[..., i+1]
        vol_diff = next_vol - this_vol
        lst.append(np.sqrt(np.sum(vol_diff ** 2) / n_voxels))
        #print(i, "appended!") #just to check it's working
    return np.array(lst)

    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    # This is a placeholder, replace it to write your solution.

def dvars_all(img):
    """ Calculate dvars metric on Nibabel image `img`

    We have tried to generalise dvar function above. Rather than comparing the differences between the 
    voxels of two volumes, this uses the basic dvar idea to compair the voxels of a volume against all 
    the others in a time series. For each volume this produces n_trials-1 (one for each comparison) 
    dvar metrics. To obtain a global dvar metric for each volume, we then re-apply the basic dvar idea 
    to compare the the n_trials-1 differences associate with a volume and return a single index of 
    differnce. 

    Warning: computationally this function is very cumbersom. Unless you really want to see it run, you 
    can find the output saved to potential_outliers.txt

    Parameters
    ----------
    img : nibabel image (4d)

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n elements, where n is the number of
        volumes in `img`.
    """
    #print(Path())
    data = img.get_fdata() 
    vx_by_time = np.reshape(data, (-1, data.shape[-1])) #flatten the volumes
    sqrt_diffs_list = []
    for i in range(vx_by_time.shape[-1]):
        print(i) # this is jsut to know where we are as we wait
        base = vx_by_time[...,i] # grab the currnet volume				
        base = np.reshape(base, (-1,1)) # making sure it has the right shape
        indexes = np.arange(0,vx_by_time.shape[-1]) # make a list of indecies (on for every volume)
        other_indexes = np.delete(indexes,i) # delete the current index from the list
        rest = vx_by_time[...,other_indexes] # use the indexes to grab every other volume
        rest_2d = np.reshape(rest, (-1,(data.shape[-1]-1))) # making sure it has the right shape
        diff = rest_2d - base #find how thier voxels differ from the base
        sqrt_of_diffs = np.sqrt(np.mean(diff ** 2, axis=0)) # find the average difference by voxel
        dbl_sqrt_of_diffs = np.sqrt(np.mean(sqrt_of_diffs ** 2, axis=0)) # find the average difference of the voxel differences
        sqrt_diffs_list.append(dbl_sqrt_of_diffs) #append
        print(dbl_sqrt_of_diffs)

    sqrt_diffs_list = np.array(sqrt_diffs_list)
    assert len(sqrt_diffs_list) == vx_by_time.shape[-1] # If this doesnt trip we have one observation per volume
    print(len(sqrt_diffs_list))
    return sqrt_diffs_list
