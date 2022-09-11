""" Test dvars implementation

You can run the tests from the root directory (containing ``README.md``) with::

    python3 -m pytest .
"""

import numpy as np

import nibabel as nib

import nipraxis as npx

from findoutlie.metrics import dvars, dvars_all



TEST_FNAME = npx.fetch_file('ds114_sub009_t2r1.nii')


def test_dvars():
    img = nib.load(TEST_FNAME)
    n_trs = img.shape[-1] #number of volumes
    n_voxels = np.prod(img.shape[:-1]) #numer of voxels in a volume
    dvals = dvars(img) # run the dvars function over the known image
    assert len(dvals) == n_trs - 1  # check that the output is one less than the number of volumes 
                                        # This is because the last (or first) volume has no comparison
    # Calculate the values the long way round
    data = img.get_fdata()
    prev_vol = data[..., 0] #get the first volume
    long_dvals = []
    for i in range(1, n_trs): #start at the 2nd element and go to the last
        this_vol = data[..., i] 
        d = this_vol - prev_vol
        long_dvals.append(np.sqrt(np.sum(d ** 2) / n_voxels))
        prev_vol = this_vol # update what the value of prev_vol
    assert np.allclose(dvals, long_dvals) # checking if the values that dvals and long_dvals get the same results

def test_dvars_all():
    img = nib.load(TEST_FNAME)   
    dvals = dvars_all(img) # run the dvars function over the known image
    data = img.get_fdata()    
    n_trs = data.shape[-1] #number of volumes in the file     
    n_vox = np.prod(data.shape[:-1]) #numer of voxels in a volume   
    assert dvals.shape[0] == n_trs  # check that the output has one value per volume in the input 
    vx_by_time = np.reshape(data, (-1, n_trs))
    assert vx_by_time.shape[0] == n_vox #check that we have the right number of voxels
    assert vx_by_time.shape[1] == n_trs #check that we have the right number of volumes
    sqrt_diffs_list = []
    for i in range(n_trs): #start at the first element and go to the end
        base = vx_by_time[...,i]
        base = np.reshape(base, (-1,1))
        indecies = np.arange(0,n_trs)
        other_indecies = np.delete(indecies,i)
        rest = vx_by_time[...,other_indecies]
        rest_2d = np.reshape(rest, (-1,(n_trs -1)))
        assert rest_2d.shape[0] == n_vox #check that the rows contain the voxels
        assert rest_2d.shape[1] == (n_trs-1) #check that the columns contain the volume comparisons
        diff = rest_2d - base 
        sqrt_of_diffs = np.sqrt(np.mean(diff ** 2, axis=0)) 
        assert sqrt_of_diffs.shape[0] == (n_trs-1) #check that we have one value per volume comparison
        dbl_sqrt_of_diffs = np.sqrt(np.mean(sqrt_of_diffs ** 2, axis=0))
        assert dvals[i] == dbl_sqrt_of_diffs
        sqrt_diffs_list.append(dbl_sqrt_of_diffs)

    sqrt_diffs_list = np.array(sqrt_diffs_list)
    assert len(sqrt_diffs_list) == n_trs
    return