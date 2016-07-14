import os
from setuptools import setup, find_packages
from pip.req import parse_requirements


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

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

packages = ['circos']

setup(name="Circos",
      version="1.3.5",
      author="Eric J. Ma, Justin Zabilansky, Jon Charest",
      author_email="ericmajinglong@gmail.com",
      description=("Circos plots in Python!"),
      license="MIT",
      keywords="network visualization, matplotlib, circos",
      url="http://github.com/ericmjl/Circos",
      packages=packages,
      install_requires=reqs,
      long_description=read('README.md'),
      classifiers=["Topic :: Scientific/Engineering :: Visualization"],
      )
