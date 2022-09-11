""" Python script to visualise scans so that we can inspect outliers

Parameters
    ----------
    data_file : str
        file with time series of volumes (relative to the wd)

    scan_position : str
        the scan in the time series that you would like to insepct

    Returns
    -------
        two images:
            one of the volume at the scan_position (printed at the middle value of the z axis)
            one of the volume at the next scan_position (printed in the same way)

Run as:

    python3 scripts/visualise_scans.py
"""

from pathlib import Path
import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

def get_scan(fname,t_position,z_value):
    img = nib.load(fname) #load the file
    data = img.get_fdata() #get the data
    i = int(t_position)
    if z_value == 'middle':
        j = int(img.shape[-2]//2 -1)
    if not z_value == 'middle':
        j = int(z_value)
    middle_slice = data[:, :, j, i] # get a 2D slice at
                                                                    # z middle position
                                                                    # time position = position arg
    return plt.imshow(middle_slice, cmap='gray')
    

#Alex: i took/adapted this bit from find_ouliers so we can access data files
def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('data_file',
                        help='A path to a data file')
    parser.add_argument('scan_position',
                        help='The volume in the time series that you want print')
    parser.add_argument('z_position',
                        nargs='?',
                        default='middle',
                        help='''The z value you want to slice the 3D image at. 
                        By defult, this will show the middle''')
    return parser


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    parser = get_parser() # Alex: i think this bit points it to the command line so we can call a file
    args = parser.parse_args()
    # Call function to find outliers.
    rows, cols = 1,2
    plt.subplot(rows, cols, 1)
    get_scan(args.data_file,args.scan_position,args.z_position)
    plt.title(f"Scan {args.scan_position}")
    plt.subplot(rows, cols, 2)
    get_scan(args.data_file,(int(args.scan_position)+1),args.z_position)
    x = (int(args.scan_position)+1)
    plt.title(f"Scan {x}")
    plt.show()
    

if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()