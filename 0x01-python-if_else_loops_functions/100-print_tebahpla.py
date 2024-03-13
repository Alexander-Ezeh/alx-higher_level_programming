#!/usr/bin/python3
# Author - Alexander Ikennaefuna Exeh

for i in range(122, 96, -1):
    if (i % 2 == 0):
        print("{}".format(chr(i)), end="")
    elif (i % 2 != 0):
        print("{}".format(chr(i-32)), end="")
