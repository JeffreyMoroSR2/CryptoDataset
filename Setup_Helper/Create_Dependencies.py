import os
import subprocess
import shutil

if os.path.isfile('requirements.txt'):
    os.remove('requirements.txt')

os.chdir('..')

subprocess.run("pipreqs --force")
shutil.move('requirements.txt', 'Setup_Helper')
