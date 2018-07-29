# coding: utf-8

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name = "watchrun",
        version = "0.1",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "restart when files changed",
        license = "MIT",
        packages=[
            'src'
        ],

        keywords = ["restart","fengyun"],
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        install_requires=['watchdog','coloredlogs'],
        data_files=[('', ['main.py'])],
        classifiers = [
             'Development Status :: 2 - Pre-Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.4',
             'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)

