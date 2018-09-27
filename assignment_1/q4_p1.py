#Word Analytics
#Part 1

import sys

if(len(sys.argv) != 3):
    print("put text here.... args..")
else:
    file_name = sys.argv[1] #first argument = file name
    n = sys.argv[2] #second argument = n
    print("file-to-open",file_name)
    print("n",n)


#get all of the file text, and separate by spaces
#for windows of n, put into dictionary, key = n-gram, value = count?


