# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-zmurray", # the name that you will install via pip
    version="1.2",
    author="Zack Murray",
    author_email="zachery.murray@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/zack-murray/lambdata-zmurray",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)