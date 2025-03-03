from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [element.strip() for element in content]

setup(
    name = "NAME SETUP.PY",
    version = "0,1",
    packages = find_packages(),
    install_requires = requirements
)
