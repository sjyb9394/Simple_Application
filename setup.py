try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name="simple_app",
    version="0.0.1",
    packages=["robot", "robot.models", "robot.controller", "robot.views"],
    package_data={"robot": ["templates/*.txt"]},
    url="",
    license="",
    author="sjyb9394",
    author_email="",
    long_description=open("README.txt").read(),
)
