
# File for general util-functions

import os


def clean_folder(folder):
    """Suppresion of the files inside the output folder"""
    filelist = os.listdir(folder)
    for filename in filelist:
        os.remove(folder + filename)


def get_the_filenames(input_folder, cut_of_data_format=False):
    """Get the filenames of the input folder as a list. Cut of data format (jpg for example), if needed."""
    filenames = sorted(os.listdir(input_folder))
    file_list = []

    for file in filenames:
        if cut_of_data_format:
            name = file[:-4]
        else:
            name = file
        file_list.append(name)

    return file_list