#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/opt/teamviewer/tv_bin/wine/drive_c/TeamViewer/tvwine.dll.so"]

    
def install():
    pisitools.insinto("/", "./opt")
    pisitools.insinto("/", "./etc")
    pisitools.insinto("/", "./usr")
    pisitools.insinto("/", "./var")

    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/teamviewerd", "etc/init.d/teamviewerd")
    pisitools.dosym("/opt/teamviewer/logfiles", "var/log/teamviewer")

    
    pisitools.dodoc("%s/opt/teamviewer/doc/License.txt" %get.workDIR())
    
    
 
    
    
    
    
