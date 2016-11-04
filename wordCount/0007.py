#!/usr/bin/python  
#-*- coding:utf-8 -*-  
__author__ = "goodhe"

#=====================================

#File Name: 0007.py
#Mail: gdhe55555@gmail.com  
#Created Time: 2016-11-03 22:48:58

#=====================================

"""
A program that can count code line numbers in a directory.
Usage: Launce the program in console with directory as argument, it can add
several directories in one time:
 $python -3 ComputeCodeLines.py <first directory> [second] [...]
    ATTENTION: use "/" in the place of "\"

 This program has been tested using some files in C and in Python,
         maybe support java as well.
"""

import os
import sys

"""
Global variables
"""
file_suffix = "not defined"
inline_comment_syntax = "not defined"
start_comment_syntax = "not defined"
end_comment_syntax = "not defined"
multilineCommentStartFlag = 0
result = {"Code files" : 0,
        "No blamk lines" : 0,
        "Code lines" : 0,
        "Comment lines" : 0,
        "Blank lines" : 0}

"""
Fuctions
"""

def getFileList(directory):
    """ Get files's list in a directory

    :directory files' directory
    :returns: file path list

    """
    file_paths = []
    for root, directories, files in os.walk(directory):
        #for direct in directories:
        #    file_paths.extend(getFileList(os.path.join(root, direct)))
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths

def getSuffix(full_file_path):
    """Get the suffix of current file.

    :full_file_path: path of one File
    :returns: suffix

    """
    return os.path.splitext(full_file_path)[1][1:]

#print getSuffix("/home/gudh/test/learn-python/README.md.ext")

def identifyFileType(suffix):
    """Identify the file type and return correct syntax.

    :suffix: file suffix
    :returns :[inline comment syntax, multiple line comment syntax]

    """
    if suffix == "py":
        return "#", "\"\"\"", "\"\"\""
    elif suffix == "c" or suffix == "h" or suffix == "cpp" or suffix == "hpp" or suffix == "cc":
        return "//", "/*", "*/"
    elif suffix == "java":
        return "//", "/*", "*/"
    else:
        return "not defined"

def isInlineComment(string_line):
    """Check if string line is an inline comment or not.

    :string_line: imput line
    :returns: true or false

    """
    commentLen = len(inline_comment_syntax)
    if string_line[0:commentLen] == inline_comment_syntax:
        return True
    else:
        return False

def isMultilineComment(string_line):
    """Check if the string line is a multiple Comment or not.

    :string_line: input line in the File
    :returns : True or False

    """
    global multilineCommentStartFlag
    commentLen = len(str(start_comment_syntax))
    if(string_line[0:commentLen] == start_comment_syntax and
            multilineCommentStartFlag == 0):
        multilineCommentStartFlag = 1
        if(len(string_line) > commentLen and
                string_line[-commentLen:] == end_comment_syntax):
            multilineCommentStartFlag = 0
        return True
    elif(string_line[0:commentLen] != start_comment_syntax and
            multilineCommentStartFlag == 1):
        if(len(string_line) > commentLen  and
                string_line[-commentLen:] == end_comment_syntax):
            multilineCommentStartFlag = 0
        return True
    elif(string_line[-commentLen:] == end_comment_syntax and 
            multilineCommentStartFlag == 1):
        multilineCommentStartFlag = 0
        return True
    else:
        return False

def countOneFile(full_file_path):
    """Count code lines in one file.

    :full_file_path: full path of the File
    :return: null

    """
    global inline_comment_syntax, start_comment_syntax, end_comment_syntax
    global multilineCommentStartFlag
    local_result = {"No blank lines": 0,
            "Comment lines":  0,
            "Code lines": 0,
            "Blank lines": 0}
    file_suffix = getSuffix(full_file_path)
    if(identifyFileType(file_suffix) != "not defined"):
        result["Code files"] += 1
        (inline_comment_syntax,
        start_comment_syntax,
        end_comment_syntax) = identifyFileType(file_suffix)
        with open(full_file_path, 'r') as lines:
            for line in lines:
                line = line.strip()
                if line.strip():
                    local_result["No blank lines"] += 1
                    if isInlineComment(line):
                        local_result["Comment lines"] += 1
                    elif isMultilineComment(line):
                        local_result["Comment lines"] += 1
                    else:
                        local_result["Code lines"] += 1
                else:
                    local_result["Blank lines"] += 1
        print(full_file_path)
        for key in local_result:
            print (str(key) + ":" + str(local_result[key]))
        result["No blank lines"] += local_result["No blank lines"]
        result["Comment lines"] += local_result["Comment lines"]
        result["Code lines"] += local_result["Code lines"]
        result["Blank lines"] += local_result["Blank lines"]

def countIndirectory(directory):
    """Count code lines in one directory.

    :directory: the directory that will be counted
    :return: null

    """

    full_file_path = getFileList(directory)
    for f in full_file_path:
        countOneFile(f)


def main():
    """main function

    """
    global file_suffix, inline_comment_syntax, start_comment_syntax
    global end_comment_syntax, multilineCommentStartFlag, result
    for directory in sys.argv[1:]:
        file_suffix = "not defined"
        inline_comment_syntax = "not defined"
        start_comment_syntax = "not defined"
        end_comment_syntax = "not defined"
        multilineCommentStartFlag = 0
        result = {"Code files": 0,
                "No blank lines": 0,
                "Code lines": 0,
                "Comment lines": 0,
                "Blank lines": 0}

        print("this is the directory: " + directory)
        countIndirectory(directory)

        print("")
        print("Final result in the directory")
        print(directory)
        for key in result:
            print(str(key) + ":" + str(result[key]))

if __name__ == "__main__":
    #print getFileList(sys.argv[1])
    main()



