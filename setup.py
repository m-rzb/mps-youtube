#!/usr/bin/python

""" setup.py for pms-youtube.

https://np1.github.com/pms-youtube

"""

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

setup(
    name="pms-youtube",
    version="0.01.07",
    description="Terminal based YouTube jukebox with playlist management",
    keywords=["video", "music", "audio", "youtube", "stream", "download"],
    author="nagev",
    author_email="np1nagev@gmail.com",
    url="http://github.com/np1/pms-youtube",
    download_url="https://github.com/np1/pms-youtube/tarball/master",
    scripts=['pmsyt'],
    install_requires=['Pafy'],
    package_data={"": ["LICENSE", "README.rst", "README"]},
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Internet :: WWW/HTTP"],
    long_description=open("README").read()
)
