#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='ghalatawi', version='0.3',
      description="ghalatawi: Arabic autocorrect library",
      long_description = readme(),      

      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://ghalatawi.sourceforge.net/',
      license='GPL',
      package_dir={'ghalatawi': 'ghalatawi'},
      packages=['ghalatawi'],
      install_requires=[ "pyarabic>=0.6.8",
            ],         
      include_package_data=True,
      package_data = {
        'ghalatawi': ['doc/*.*','doc/html/*', 'data/*.acl', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

