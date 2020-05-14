# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-jiobu1",  # the name that you will install via pip
    version="1.11",
    author="Jisha Obukwelu",
    author_email="jisha-obukwelu@lambdastudents.com",
    description="Enlarge Function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/jiobu1/lambdata-jiobu1",
    # keywords="",
    packages=find_packages()  # find_packages() #['my_lambdata']
)
