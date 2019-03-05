import sys
import datetime
import argparse

def argparser(args):
    parser = argparse.ArgumentParser(description='Simple Line by Line Compare Tool between two text file')
    parser.add_argument('file1', help='first file to compare')
    parser.add_argument('file2', help='second file to compare')
    #parser.add_argument('--listdifferent', type=bool, default=False, action='store_true', help='List only different')
    return parser.parse_args(args)

def main(arguments):

    list1 = None
    list2 = None

    try:
        filehandler = open(arguments.file1)
        list1 = filehandler.readlines()
        filehandler = open(arguments.file2)
        list2 = filehandler.readlines()
    except Exception as ex:
        print(ex)

    #Strip eol and space trailing
    list1 = list(map(lambda s: s.strip(),list1))
    list2 = list(map(lambda s: s.strip(),list2))

    index = 1
    for l in list1:
        if l not in list2:
            print("List1 Line: {0} does not exist in List2, value: {1}".format(index,l))
        index += 1
    
    index = 1
    for l in list2:
        if l not in list1:
            print("List2 Line: {0} in  does not exist in List1, value: {1}".format(index,l))
        index += 1


if __name__ == '__main__':
    argv = argparser(sys.argv[1:])
    main(argv)