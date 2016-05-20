import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="Circos",
      version="1.1",
      author="Eric J. Ma, Justin Zabilansky, Jon Charest",
      author_email="ericmajinglong@gmail.com",
      description=("Circos plots in Python!"),
      license="MIT",
      keywords="network visualization, matplotlib, circos",
      url="http://github.com/ericmjl/Circos",
      packages=[],
      data_files=['README.md'],
      long_description=read('README.md'),
      classifiers=["Topic :: Scientific/Engineering :: Visualization"],
      )
