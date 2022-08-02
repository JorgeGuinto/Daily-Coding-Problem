# Suppose we represent our file system by a string in the following manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext

# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

def findDeepestFile(directory):
    fileP = directory.find(".")
    if fileP < 0:
        print("There is no file in de directory")
        return -1
    
    file = True
    maxCount = 1
    deepestFileS = directory.rfind("\t", 0, fileP)
    tempFileP = fileP
    while file:
        keep = True
        count = 1
        fileS = directory.rfind("\t", 0, tempFileP)

        while keep:
            if directory[fileS-1] == "\t":
                count += 1
                fileS -= 1
            else:
                keep = False
        
        #Update Max shifts
        if count > maxCount:
            deepestFileS = fileS
            maxCount = count
            fileP = tempFileP
        
        #Check next file
        if directory.find(".", tempFileP+1) < 0:
            file = False
        else:
            tempFileP = directory.find(".", tempFileP+1)

    fileEnd = directory.find("\n", fileP)
    if fileEnd < 0:
        deepestDirectory = '' + directory[deepestFileS-1:]
    else:
        deepestDirectory = '' + directory[deepestFileS-1:fileEnd]
    
    while maxCount > 1:
        subF = '\t'
        for i in range(maxCount-2):
            subF = subF + "\t"
        searchS = directory.rfind(subF, 0, deepestFileS)    
        while directory[searchS + maxCount - 1] == '\t' or directory[searchS - 1] != '\n':
            searchS = directory.rfind(subF, 0, searchS)
        
        deepestDirectory = directory[searchS-1:directory.find('\n', searchS)] + deepestDirectory
        maxCount -= 1
        
    deepestDirectory = directory[:directory.find('\n')] + deepestDirectory
    print(deepestDirectory)
    otherPrint(deepestDirectory)
    return deepestDirectory
    
def otherPrint(directory):
    directory = directory.replace('\n', '/')
    directory = directory.replace('\t', '')
    print(directory)

w = "dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\nsubValiendo"
y = "0123 4 56789d12 3 4 56789v12345 6 7 89t1234567 8 9c123456 7 8 9c123456789 s 1 2 3456789t12 3456789o123"
a = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
b = "dir\n\tC1\n\t\tC11\n\t\t\tAr1.1\n\tC2\n\t\tC21\n\t\t\tAr211.py\n\t\t\tAr212.py\n\t\tC22\n\t\tC23\n\t\t\tC231\n\t\t\t\tC2311\n\t\t\t\t\tAr2311.py\n\tC3\n\t\tC31\n\t\tC32\n\t\t\tAr321.py"

findDeepestFile(b)