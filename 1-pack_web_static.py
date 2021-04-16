#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
from AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """compress files"""
    time = datetime.now()
    timeDate = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timeDate))
        return("versions/web_static_{}.tgz".format(timeDate))
    except:
        return None
