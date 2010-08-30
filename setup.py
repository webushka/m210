# -*- coding: utf-8 -*-

import errno
import os

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup, Extension

class build_py(_build_py):
    """Generate Python-modules from .ui files."""

    def run(self):
        try:
            filenames = os.listdir('qt/ui')
        except OSError, e:
            if e.errno == errno.ENOENT:
                # ui directory does not exists. fine, no ui-files then.
                filenames = []
            raise e # Something else went wrong during listing, panic!

        # qt/ui/*.ui -> qt/src/lib/ui/*.py
        for filename in os.listdir('qt/ui'):
            filename = os.path.basename(filename)
            name, ext = os.path.splitext(filename)
            if ext != '.ui':
                continue
            src_path = 'qt/ui/%s' % filename
            source_mtime = os.stat(src_path).st_mtime
            dest_path = 'qt/src/lib/ui/%s.py' % name
            if not os.path.exists(dest_path):
                dest_mtime = -1
            else:
                dest_mtime = os.stat(dest_path).st_mtime
            if source_mtime > dest_mtime:
                os.system('pyuic4 -o qt/src/lib/ui/%s.py qt/ui/%s' % (name, filename))

        return _build_py.run(self) # Proceed normally.

modulehidraw = Extension('m210.hidraw',
                         sources=['pylib/src/lib/modulehidraw.c'])

moduleinput = Extension('m210.input',
                         sources=['pylib/src/lib/moduleinput.c'])

setup(name='m210',
      version='0.2',
      author='Tuomas Räsänen',
      author_email='tuos@codegrove.org',
      package_dir={ # One for each module.
        'm210':        'pylib/src/lib',
        'm210.daemon': 'daemon/src/lib',
        'm210.cli':    'cli/src/lib',
        'm210.qt':     'qt/src/lib',
        },
      packages=[
        'm210',
        'm210.cli',
        'm210.daemon',
        'm210.qt',
        'm210.qt.ui',
        ],
      scripts=[
        'daemon/src/bin/m210-daemon',
        'cli/src/bin/m210-connect',
        'cli/src/bin/m210-disconnect',
        'cli/src/bin/m210-download',
        'cli/src/bin/m210-info',
        'cli/src/bin/m210-erase',
        'qt/src/bin/m210-qt',
        ],
      data_files=[
        ('/etc/dbus-1/system.d',
         [
                'daemon/etc/dbus-1/system.d/org.codegrove.m210.daemon.conf',
                ],
         ),
        ('/etc/init',
         [
                'daemon/etc/init/m210-daemon.conf',
                ],
         ),
        ('/etc/udev/rules.d',
         [
                'daemon/etc/udev/rules.d/50-m210-daemon.rules',
                ],
         ),
        ],
      cmdclass={
        'build_py': build_py,
        },
      ext_modules=[modulehidraw, moduleinput],
      )