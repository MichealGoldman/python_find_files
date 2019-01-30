"""
    Title: pysearch
    Author: Harold Goldman
    Email: mikerah@gmail.com
    Date: 1/29/2019
    Description: Search for files in system
    Version: 0.0.1
"""

import os
import argparse
from collections import OrderedDict


def search_contains(ARGS):
    """
    Match if string is within filename
    Arguments: 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    file_list = []
    file_list.append("All files with {} in folder {} \n".format(ARGS.file, ARGS.path))
    for (paths, dirs, files) in os.walk(ARGS.path):
        for file in files:
            if ARGS.file in file:
                file_list.append(os.path.join(paths, file))
    return(file_list)


def search_starts(ARGS):
    """
    Match if filename starts with string
    Arguments: 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    file_list = []
    file_list.append("All files starting with {} in folder {} \n".format(ARGS.file, ARGS.path))
    for (paths, dirs, files) in os.walk(ARGS.path):
        for file in files:
            if file.startswith(ARGS.file):
                file_list.append(os.path.join(paths, file))
    return(file_list)


def search_ends(ARGS):
    """
    Match if filename ends with string
    Arguments: 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    file_list = []
    file_list.append("All files ending with {} in folder {} \n".format(ARGS.file, ARGS.path))
    for (paths, dirs, files) in os.walk(ARGS.path):
        for file in files:
            if file.endswith(ARGS.file):
                file_list.append(os.path.join(paths, file))
    return(file_list)


def search_matches(ARGS):
    """
    Match if string and filename are exact match
    Arguments: 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    file_list = []
    file_list.append("All files matching {} in folder {} \n".format(ARGS.file, ARGS.path))
    for (paths, dirs, files) in os.walk(ARGS.path):
        for file in files:
            if ARGS.file == file:
                file_list.append(os.path.join(paths, file))
    return(file_list)


def print_list(file_list, ARGS):
    """
    Print results to screen
    Arguments:
        file_list -- {list} 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    print("\tFound {} files containing {} in {}".format(len(file_list) - 1, ARGS.file, ARGS.path))
    for file in file_list:
        print("\t\t{}".format(file))


def create_file(file_list, ARGS):
    """
    Print results to file
    Arguments:
        file_list -- {list} 
        ARGS -- {ArgumentParser Args}
    Returns:
        file_list {list}
    """
    
    with open(ARGS.o, "w") as outfile:
        outfile.write("\tFound {} files containing {} in {}".format(len(file_list) - 1, ARGS.file, ARGS.path))
        for found in file_list:
            outfile.write("\n\t{}".format(found))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="\tSearch for files")
    PARSER.add_argument("path", help="the inital path to search")
    PARSER.add_argument("file", help="the filename or partial filename you are looking for")
    PARSER.add_argument("-c", help="file contains", action="store_true")
    PARSER.add_argument("-s", help="file starts with", action="store_true")
    PARSER.add_argument("-e", help="file ends with", action="store_true")
    PARSER.add_argument("-m", help="file matches -- default if no others selected", action="store_true")
    PARSER.add_argument("-o", help="output file -- prints to screen if not set")
    
    ARGS = PARSER.parse_args() 

    search_type = OrderedDict({ "c": search_contains
                    , "s": search_starts
                    , "e": search_ends
                    , "m": search_matches
                    })

    choice = vars(ARGS)

    for key, value in vars(ARGS).iteritems():

        if choice[key] == True and key and vars(ARGS)["o"] is not None :
            create_file(search_type[key](ARGS), ARGS)
        if choice[key] == True and key and vars(ARGS)["o"] is None:
            print_list(search_type[key](ARGS), ARGS)
        # print(key, vars(ARGS)[key])
