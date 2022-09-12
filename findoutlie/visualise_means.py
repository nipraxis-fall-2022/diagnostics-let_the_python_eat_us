""" Helper function to plot volume means for each 4D image

Parameters
    ----------
    data_file : str
        .nii.gz file 

    Returns
    -------
        plot of volume means

"""

import numpy as np 
import matplotlib.pyplot as plt 
import nibabel as nib



def plot_volume_means(fname):
	img = nib.load(fname)
	data = img.get_fdata()
	n_trs = img.shape[-1]
	means = []
	for vol_no in range(n_trs):
		vol = data[..., vol_no]
		means.append(np.mean(vol))

	return plt.plot(means)
