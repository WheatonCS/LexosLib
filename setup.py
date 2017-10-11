"""This file is used for pip install"""

from setuptools import setup, find_packages

from proj_info import SHORT_NAME, VERSION, AUTHOR, LICENSE_TYPE, \
    SHORT_DESCRIPTION, LONG_DESCRIPTION

setup(
    name=SHORT_NAME,
    version=VERSION,
    license=LICENSE_TYPE,
    author=AUTHOR,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'numpy',
        'scikit-learn',
        'scipy',
        'pandas',
        'gensim',
        'beautifulsoup4',
        'lxml',
        'matplotlib',
        'chardet',
        'natsort'
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education :: Text Processing :: Utilities'
    ]
)
