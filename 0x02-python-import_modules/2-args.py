#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))

    if argc >= 1:
        argc = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(argc, arg))
            argc += 1

#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

if num_args > 0:
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
