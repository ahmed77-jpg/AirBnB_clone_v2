#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local
from datetime import datetime

def do_pack():
    """
    function creates a .tgz
    """
    local("mkdir -p versions")
    rtat = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if rtat.failed:
        return None
    return rtat
