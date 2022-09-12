""" Python script to find outliers

Run as:

    python3 scripts/find_outliers.py data
"""

from pathlib import Path
import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter

# Put the findoutlie directory on the Python path.
PACKAGE_DIR = Path( __file__ ).parents[1]
sys.path.append(str(PACKAGE_DIR))

from findoutlie import outfind
from findoutlie.metrics import dvars, dvars_all
from findoutlie.mahal import mahal


def print_outliers(data_directory, method):
    # adding a section so if anyone tests out our code, data can be loaded from any directory
    try:
        #first check the example data are loaded, if not try the different directory specified
        assert sys.argv[1] == Path.joinpath(PACKAGE_DIR, "data").name
    except:
        try:
            #check whether the different directory specified has the right file type, if not try again with full path
            assert len(list(Path(sys.argv[1]).rglob("*.nii.gz"))) > 0
        except:
            dir_to_load_confirmed = input(
                "These are not the example data and the input directory doesn\'t have the right file type. Confirm path on your system: ")  # no quotes
            data_directory = dir_to_load_confirmed
    if method == dvars:
        outlier_dict = outfind.find_outliers(data_directory, dvars)
    elif method == dvars_all:
        outlier_dict = outfind.find_outliers(data_directory, dvars_all)
    else:
        outlier_dict = outfind.find_outliers(data_directory, mahal)
    for fname, outliers in outlier_dict.items():
        if len(outliers) == 0:
            continue
        outlier_strs = []
        for out_ind in outliers:
            outlier_strs.append(str(out_ind))
        print(', '.join([str(fname)] + outlier_strs))


def get_parser():
    method_keys = {'dvars': dvars,
                    'dvars_all': dvars_all,
                    'mahal': mahal}
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('data_directory',
                        help='Directory containing data')
    parser.add_argument('method',choices=method_keys.keys(),
                        help='Specify which method to use. Currently: dvars, dvars_all, or mahal')
    return parser


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    parser = get_parser()
    args = parser.parse_args()
    # Call function to find outliers.
    print_outliers(args.data_directory, args.method)



if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
