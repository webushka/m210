# -*- coding: utf-8 -*-

from distutils.core import setup

import noter

setup(name='noter-cli',
      version=noter.VERSION,
      author='Tuomas Räsänen',
      author_email='tuos@codegrove.org',
      package_dir={'noter.cli': 'src/lib'},
      packages=['noter.cli'],
      scripts=[
        'src/bin/noter-connect',
        'src/bin/noter-disconnect',
        ],
      )
