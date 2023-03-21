import subprocess
import os

def run_bat(filename):
    subprocess.call([filename])

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_bat('YouCut.bat')