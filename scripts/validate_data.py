""" Python script to validate data

Run as:

    python3 scripts/validate_data.py
"""

from pathlib import Path
import hashlib


def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    # Calculate, return SHA1 has on the bytes from the file.
    # This is a placeholder, replace it to write your solution.
    raise NotImplementedError(
        
        'This is just a template -- you are expected to code this.')


def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    #A Get the normal librarys (we can remove extras later)
    
    #gets path function
    from pathlib import Path
    #gets hash function
    from hashlib import sha1

    # Read lines from ``data_hashes.txt`` file.
    scripts_path = Path()
    folder_path = scripts_path.parent
    data_path = folder_path / 'data'
    hash_path = data_path / 'group-02' / 'hash_list.txt'

    #Chekcing the file at the example path exits
    if not hash_path.is_file():
        raise RuntimeError('There is an issue with your paths')
    
    #Read in the text
    hash_fname_text = hash_path.read_text()

    #Split the text into lines
    split_lines = hash_fname_text.splitlines()
    # Split into SHA1 hash and filename
        #a Dumb way to check that this ran correctly
        #yeses = []
    for line in split_lines:
        # Split each line into expected_hash and filename
        fhash, fname = line.split() 
        fpath = data_path / fname
        # Calculate actual hash for given filename.
        # To do this we read the data
        fcontents = fpath.read_bytes()
        # then calcuate the expected hash
        expectedhash = sha1(fcontents).hexdigest()
        if not expectedhash == fhash:
        # If hash for filename is not the same as the one in the file, raise Value Error
            return ValueError
            # A dumb way to check that this ran correctly again
            #if expectedhash == fhash: 
            #    yeses.append('Yes')
    return 
    raise NotImplementedError(
        'This is just a template -- fill out the template with code.')


def main():
    # This function (main) called when this file run as a script.
    group_directory = (Path(__file__).parent.parent / 'data')
    groups = list(group_directory.glob('group-??'))
    if len(groups) == 0:
        raise RuntimeError('No group directory in data directory: '
                           'have you downloaded and unpacked the data?')

    if len(groups) > 1:
        raise RuntimeError('Too many group directories in data directory')
    # Call function to validate data in data directory
    validate_data(groups[0])


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
