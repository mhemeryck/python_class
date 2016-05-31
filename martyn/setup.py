from setuptools import setup

import labelbox


def readme(filename='README.md'):
    """return README contents"""

    with open(filename, 'r') as fh:
        return fh.read()


def requirements(filename='requirements.txt'):
    """return install requirements"""

    with open(filename, 'r') as fh:
        return fh.read().splitlines()


setup(
    name=labelbox.__name__,
    version=labelbox.__version__,
    author=labelbox.__author__,
    url='http://www.soundtalks.com',
    packages=['labelbox'],
    description='python ORM example',
    long_description=readme(),
    install_requires=requirements(),
)
