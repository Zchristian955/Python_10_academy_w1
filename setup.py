!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Christian",
    email="zanouchristian955@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Repository structure for all your project",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='script',
    name='script',
    packages=find_packages(include=['script', 'script.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='github.com/Zchristian955/Python_10_academy_w1',
    version='0.1.0',
    zip_safe=False,
)
