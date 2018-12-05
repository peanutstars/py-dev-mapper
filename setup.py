from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", 'r') as fd:
    version = fd.read().strip()

setup(
    name='dev-mapper',
    version=version,
    description='Device Mapper to convert the sys-pci-address to a device file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='HyunSuk Lee',
    author_email='peanutstars.job@gmail.com',
    scripts=[
    ],
    keywords='dev path convert',
    packages=['devmapper'],
    data_files = [('.', ['VERSION', 'Makefile'])],
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Manufacturing',
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Operating System Kernels :: Linux",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
    ],
    setup_requires=[
    ],
)
