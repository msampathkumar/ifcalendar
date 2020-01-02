from setuptools import setup

description = '''In most time based statistical analysis, generating reports by month or week is a common practice. But the standard Georgian Calendar Months, have differences in each month and adding more concerns by generating in accurate analysis. IFC solves these challenges by having fixed months. In this package, we offer required tools to convert Georgian dates to IFC.'''

setup(
    name='ifcalendar',
    version='0.1',
    description=description,
    author='Sampath Maddula',
    author_email='sam1990kumar@gmail.com',
    packages=['ifcalendar'],
    install_requires=[],
)
