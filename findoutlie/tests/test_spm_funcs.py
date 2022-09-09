""" Test script for SPM functions

Run these tests with::

    python3 findoutlie/tests/test_spm_funcs.py

or better, in IPython::

    %run findoutlie/tests/test_spm_funcs.py
"""

from pathlib import Path
import sys

MY_DIR = Path(__file__).parent
EXAMPLE_FILENAME = 'ds107_sub012_t1r2_small.nii'

# Here you should add the directory containing the findoutlie
# directory to the Python path.
# Hint: sys.path
# Hint: see the solutions if you are stuck.
# +++your code here+++

import numpy as np

import nibabel as nib

# This import needs the directory containing the findoutlie directory
# on the Python path.
from findoutlie.spm_funcs import get_spm_globals, spm_global # Had to add <findoutlie.> to get it work


def test_spm_globals():
    # Test get_spm_globals and spm_global functions
    example_path = MY_DIR / EXAMPLE_FILENAME # these are defined for a specific test file
    expected_values = np.loadtxt(MY_DIR / 'global_signals.txt') # known values they gave us
    glob_vals = get_spm_globals(example_path) # run our function (for an entier file)
    assert glob_vals is not None, 'Did you forget to return the values?'
    assert np.allclose(glob_vals, expected_values, rtol=1e-4) #check out put matches expected
    img = nib.load(example_path)
    data = img.get_fdata()
    globals = []
    for vol_no in range(data.shape[-1]): # for each volume in the time series
        vol = data[..., vol_no] # get the volume
        globals.append(spm_global(vol)) # get the spm for a specific volume
    assert np.allclose(globals, expected_values, rtol=1e-4) # check output matchs the expected values


if __name__ == '__main__':
    # File being executed as a script
    test_spm_globals()
    print('Tests passed')
