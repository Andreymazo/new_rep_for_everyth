import os
import contextlib


class ChangeDir:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        pass
        # return self

    def __exit__(self, exc_type, exc_val, traceback):
        pass


with ChangeDir('dir1'):
    print("1. Текущая деректория:", os.getcwd())
    os.chdir('dir1')
    print(os.listdir())

with ChangeDir('dir2'):
    print("2. Текущая деректория:", os.getcwd())
    os.chdir('..')
    print("2. Текущая деректория:", os.getcwd())
    print(os.listdir('dir2'))

# вывод в консоль
# ['log.txt']
# ['file1.py', 'file2.py']
