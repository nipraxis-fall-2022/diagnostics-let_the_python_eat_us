""" Test dvars implementation

You can run the tests from the root directory (containing ``README.md``) with::

    python3 -m pytest .
"""

import numpy as np

import nibabel as nib

import nipraxis as npx

from findoutlie.metrics import dvars



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


