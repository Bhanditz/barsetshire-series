# -*- coding: UTF-8 -*-

# script for splitting text files

# in order to run this, navigate to where the script lives
# and type this command. Note the regular expression needs to be
# wrapped in single quotes
#
#      $ python txt-split [path to textfile] [regular expression]

import os
import re
from sys import argv

# list of regular possible expressions
# \nCHAPTER [A-Z]*\n
# \n– [A-Z]* –

#helper function to write to file
#   string filename, original text file
#   int count, section number
#   string text, text to write
def write_file(filename, count, text):

    file_out = filename + '_' + format(count,'03d') + '.txt'
    f = open(file_out, 'w')
    print('writing ' + file_out)
    f.write(text)
    f.close()

#splits longer text into sections according to a regular
#expression, creates a directory, writes sections to that directory
#   string file_in, filename of the longer text
#   string regex, regex expression
def regex_split(path_in, regex):

    count = 0
    f_in = open(path_in,'r')
    path_list = path_in.split('/')
    filename = path_list.pop()[:-4]
    dir_leaf = filename + '_split'
    dir_branch = '/'.join(path_list) if (len(path_list) > 0) else '.'

    text = f_in.read()
    f_in.close()

    # make a new directory from the filename
    if dir_leaf not in os.listdir(dir_branch):
        os.mkdir('/'.join([dir_branch,dir_leaf]))

    # # split long text into array of sections
    sections = re.split(regex,text)

    for section in sections:
        if len(section) > 1:
    #         #write each section to a new file
            count += 1
            file_out = '/'.join([dir_branch,dir_leaf,filename])
            write_file(file_out, count, section)

if __name__ == '__main__':

    # takes two arguments, the filename and the regular expression
    regex_split(argv[1],argv[2])