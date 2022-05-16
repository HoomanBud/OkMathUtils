from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='openmathutils',
    version='0.1.2',
    description='Simple math utilities for python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Hooman Bud',
    author_email='hoomanbud5511@gmail.com',
    url='https://github.com/ncthuc/elastictools',
)