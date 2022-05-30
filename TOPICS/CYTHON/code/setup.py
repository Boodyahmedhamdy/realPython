# from setuptools import setup
# from Cython.Build import cythonize
#
# setup(
#     ext_modules=cythonize("main.pyx")
# )
import distutils.core
import Cython.Build
distutils.core.setup(
    ext_modules=Cython.Build.cythonize("main.pyx"))
