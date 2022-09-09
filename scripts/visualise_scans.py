""" Python script to visualise scans so that we can inspect outliers

Parameters
    ----------
    data_file : str
        file with time series of volumes (relative to the wd)

    scan_position : str
        the scan in the time series that you would like to insepct

    Returns
    -------
        an image of that volume (printed at the middle value of the z axis)

Run as:

    python3 scripts/visualise_scans.py
"""

from pathlib import Path
import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

def get_scan(position,fname):
    img = nib.load(fname) #load the file
    data = img.get_fdata() #get the data
    i = int(position)
    middle_slice = data[:, :, (img.shape[-2]// 2 - 1), i] # get a 2D slice at
                                                                    # z middle position
                                                                    # time position = position arg
    return plt.imshow(middle_slice, cmap='gray')
    

#Alex: i took/adapted this bit from find_ouliers so we can access data files
def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('scan_position',
                        help='the volume in the time series that you want print')
    parser.add_argument('data_file',
                        help='A path to a data file')
    return parser


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    parser = get_parser() # Alex: i think this bit points it to the command line so we can call a file
    args = parser.parse_args()
    # Call function to find outliers.
    get_scan(args.scan_position,args.data_file)
    plt.show()
    

if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()