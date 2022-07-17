#Given a file path (absolute or relative), the program should write to a file all of the
# contents of the directory and the child directories bellow it.

import os
path = os.getcwd()

for path, names, files in os.walk(path):
    for file in files:
        print(os.path.join(path, file))