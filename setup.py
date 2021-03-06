from setuptools import find_packages, setup

__version__ = '0.3.0-dev0'


setup(
  name='pesos',
  version=__version__,
  description='Pure python implementation of the Apache Mesos Framework API',
  url='http://github.com/wickman/pesos',
  author='Brian Wickman',
  author_email='wickman@gmail.com',
  license='Apache License 2.0',
  packages=find_packages(exclude=['tests']),
  install_requires=[
    'compactor[pb]==0.3.0',
    'futures==2.1.6',
    'mesos.interface==0.21.1',
  ],
  extras_require={
    'zk': ['twitter.common.zookeeper==0.3.3'],
  },
  zip_safe=True
)
