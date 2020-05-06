"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import platform
import os

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(sys.argv)
arguments = len(sys.argv) - 1
positions = 1
while (arguments >= positions):
    print("parameter %i: %s" % (position, sys.argv[positions]))
    positions = positions + 1

for key, value in sys.modules.items():
    print(value)

for i in sys.argv:
    print(i)

# Print out the OS platform you're using:
print(sys.platform)
print(platform.system())
print(os.name)

# Print out the version of Python you're using:
print(sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getuid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.uname()[1])
