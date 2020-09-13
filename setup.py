from distutils.core import setup
from os import path
import os

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))

description = 'This library has several helper functions for deep learning

try:
    with open(path.join(this_directory, 'kdlutils/README.rst'), "r") as f:
        long_description = f.read()
except:
    long_description = description

setup(
  name = 'kdlutils',         # How you named your package folder
  packages = ['kdlutils'],   # Chose the same as "name"
  version = '1.4.9',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = description,
  long_description=long_description,
  long_description_content_type="text/x-rst",
  author = 'kaustubh sadekar',                   # Type in your name
  url = 'https://github.com/kaustubh-sadekar/githubActions',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kaustubh-sadekar/githubActions/archive/v_1.4.9.tar.gz',    # I explain this later on
  keywords = ['Deep Learning', 'Helper functions'],   # Keywords that define your package best
  package_data={'':['README.rst']},
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

