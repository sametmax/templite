# -*- coding: utf-8 -*-



from setuptools import setup, find_packages


setup(

    name="templite",
    version="0.1.4",
    py_modules=['templite'],
    author="Sam et Max",
    author_email="lesametlemax@gmail.com",
    description="A light-weight, fully functional, general purpose Python templating engine that fits in one single file.",
    long_description=open('README.rst').read(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
    ],
    url="http://www.joonis.de/en/code/templite"
)

