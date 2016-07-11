import os
from setuptools import setup


def read(fname):
    """
    Utility function to read the README file. Used for the
    long_description.  It's nice, because now:
    1. we have a top level README file and
    2. it's easier to type in the README file than to put a raw
       string in below ...
    """
    return open(
        os.path.join(os.path.dirname(__file__), fname)
        ).read()

setup(name="Circos",
      version="1.3.4",
      author="Eric J. Ma, Justin Zabilansky, Jon Charest",
      author_email="ericmajinglong@gmail.com",
      description=("Circos plots in Python!"),
      license="MIT",
      keywords="network visualization, matplotlib, circos",
      url="http://github.com/ericmjl/Circos",
      # packages=find_packages(),
      py_modules=['circos'],
      # package_data={'': ['README.md', 'requirements.txt']},
      install_requires=['matplotlib',
                        'numpy',
                        'setuptools',
                        'pycodestyle'],
      long_description=read('README.md'),
      classifiers=["Topic :: Scientific/Engineering :: Visualization"],
      )
