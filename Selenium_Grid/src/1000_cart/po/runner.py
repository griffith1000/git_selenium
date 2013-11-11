
import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('src'):
  for filename in fnmatch.filter(filenames, '*.c'):
      matches.append(os.path.join(root, filename))





from subprocess import Popen
import glob
tests = glob.glob('test*.py')
processes = []
for test in tests:
    processes.append(Popen('python %s' % test, shell=True))
for process in processes:
    process.wait()