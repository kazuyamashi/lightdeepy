import os
from setuptools import setup, find_packages  
version = '0.1.0'
# script_name = 'crecomp'
def read(filename):
    return open(os.path.join(os.path.dirname(__file__),filename)).read()
print find_packages()
import sys
setup(
        name='lightdeepy',
        version=version,
        description="Light Deep Learning on Python", 
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Code Generators",
            "License :: OSI Approved :: BSD License",
            ],
        keywords='deep learning',
        author="Kazushi Yamashina",
        author_email="kazuyamashi_at_gamil.com",
        url='https://github.com/kazuyamashi/lightdeepy.git',
        license='new BSD',
        packages=find_packages(),
        # package_data={ },
        long_description=read('README.rst'),
        # install_requires=["jinja2", "veriloggen", "pyverilog"],
        # entry_points = 
        # [console_scripts]
        # %s = crecomp.crecomp:main
        #  % script_name,
    )