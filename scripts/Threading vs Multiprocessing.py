# A process can have multi thread inside them
# Process doesn't share data b/w other Process
# Process is started independently from other processes
# Process is heavy weight than thread..

# Thread is a light weight process
# Threading is limited by GIL..
# Threading are not killable and interruptable..
# Careful with race condition

# GIL : global interpretor lock..
# lock that allows one thread at a time to execute in python
# Needed in Cpython because memory management is not thread safe..
# Avoid : 1) use multiprocessing... 2) use jython and ironpython...

# Multi-processing

from multiprocessing import Process
from threading import Thread
import os

# For processes : create > start > join 
# For threading : create > start > join (wait for them to complete.. threads to complete...)
