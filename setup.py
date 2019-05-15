import re
from os.path import join, dirname
from setuptools import setup, find_packages

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'barcodeutil', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


dependencies = [
    'opencv-python',
    'easycli',
    'zxing'
]


setup(
    name='barcodeutil',
    version=package_version,
    author='Carrene',
    author_email='shiva@carrene.com',
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'barcodeutil = barcodeutil.cli:Main'
        ]
    },
    packages=find_packages(),
)
