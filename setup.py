desc = """\
pyFRF
======

Frequency response function as used in structural dynamics.
-----------------------------------------------------------
This package is part of the www.openmodal.com project.

For a showcase see: https://github.com/openmodal/pyFRF/blob/master/Showcase%20pyFRF.ipynb
"""

#from distutils.core import setup, Extension
from setuptools import setup, Extension
setup(name='pyFRF',
      version='0.1.2',
      author='Janko Slavič',
      author_email='janko.slavic@fs.uni-lj.si',
      url='https://github.com/openmodal/pyFRF',
      py_modules=['pyFRF'],
      #ext_modules=[Extension('lvm_read', ['data/short.lvm'])],
      long_description=desc,
      requires=['numpy']
      )