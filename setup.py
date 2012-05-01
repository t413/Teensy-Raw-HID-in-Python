#!/usr/bin/env python

from distutils.core import setup, Extension
import platform, sys


if platform.system() == 'Linux':
    rawhidmodule = Extension('TeensyRawhid',
        sources = ['teensyrawhid/rawhidmodule.c', 'teensyrawhid/hid_LINUX.c'],
        extra_link_args = ['-lusb']
    )

elif platform.system() == 'Darwin':
    rawhidmodule = Extension('TeensyRawhid',
        sources = ['teensyrawhid/rawhidmodule.c', 'teensyrawhid/hid_MACOSX.c'],
        extra_link_args = ['-framework', 'IOKit', '-framework', 'CoreFoundation']
    )
    
elif platform.system() == 'Windows':
    rawhidmodule = Extension('TeensyRawhid',
        sources = ['teensyrawhid/rawhidmodule.c', 'teensyrawhid/hid_WINDOWS.c'],
        extra_link_args = ['-lhid', '-lsetupapi']
    )
    #TODO Test on windows
else: raise Exception('Unknown OS')

setup(
    name='TeensyRawhid',
    version='0.1.0',
    author='Ian Howson',
    author_email='ian@mutexlabs.com',
    #packages=['teensyrawhid'],
    description='Raw HID client for Teensy development boards',
    url='http://mutexlabs.com/c/TeensyRawhid/',
    download_url='http://mutexlabs.com/c/TeensyRawhid/download/teensyrawhid-0.1.0.tar.gz',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows NT/2000",
        "Topic :: Software Development :: Embedded Systems",
    ],
    scripts=[],
    long_description=open('README.txt').read(),
    ext_modules = [rawhidmodule]
)

