# -*- coding: utf-8 -*-
# m210
# Copyright © 2010 Tuomas Räsänen (tuos) <tuos@codegrove.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

# Standard modules.
import os.path
import sys

# Third-party modules.
import dbus.exceptions

# Project modules.
import m210.daemon

def error_and_exit(msg):
    prog = os.path.basename(sys.argv[0])
    print("%s: error: %s" % (prog, msg), file=sys.stderr)
    sys.exit(1)

def get_interface_or_exit():
    try:
        return m210.daemon.Interface()
    except dbus.exceptions.DBusException, e:
        if e.get_dbus_name() == "org.freedesktop.DBus.Error.ServiceUnknown":
            error_and_exit("%s is not available" % m210.daemon.NAME)
        raise e