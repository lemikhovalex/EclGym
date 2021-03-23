from setuptools import setup
import pkg_resources
from setuptools import find_namespace_packages

setup(
    name='ecl_gym',
    author_email='lemikhovalex@gmail.com',
    description='Package with gym-like env for petroleum reservoir simulation',
    packages=find_namespace_packages(
        where=['ecl_gym', 'ecl_gym.*']
    ),
)
