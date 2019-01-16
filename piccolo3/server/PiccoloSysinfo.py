# Copyright 2018- The Piccolo Team
#
# This file is part of piccolo3-server.
#
# piccolo3-server is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# piccolo3-server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with piccolo3-server.  If not, see <http://www.gnu.org/licenses/>.

"""
.. moduleauthor:: Magnus Hagdorn <magnus.hagdorn@ed.ac.uk>

"""

from PiccoloComponent import PiccoloBaseComponent
import psutil
import socket
from datetime import datetime
from pytz import utc

class PiccoloSysinfo(PiccoloBaseComponent):
    """piccolo system information"""
    
    LOGBASE = 'sysinfo'

    def get_cpu(self):
        """get cpu usage (percent)"""
        return psutil.cpu_percent()
    def get_mem(self):
        """get memory usage (percent)"""
        return psutil.virtual_memory().percent
    def get_host(self):
        """get hostname"""
        return socket.gethostname()
    def get_clock(self):
        """get the current date and time"""
        return datetime.now(tz=utc).isoformat()

if __name__ == '__main__':
    from piccoloLogging import *
    piccoloLogging(debug=True)

    ps = PiccoloSysinfo()
    print (ps.get_cpu())
    print (ps.get_mem())
    print (ps.get_host())
    print (ps.get_clock())
    