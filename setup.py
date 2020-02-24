from setuptools import setup

description = 'Cotsworth Calendar or International Fixed Calendar for Statistical Analysis and Experiments'
long_description = ''

with open('INTRO.md') as fp:
    long_description = fp.read()

setup(
    name='ifcalendar',
    version='0.1.3',
    author='Sampath Maddula',
    author_email='sam1990kumar@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['ifcalendar'],
    url='https://github.com/msampathkumar/ifcalendar',
    install_requires=[],
)
