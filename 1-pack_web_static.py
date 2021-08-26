#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """web_static"""
    tgz = datetime.now().strftime("%Y%m%d%H%M%S")
    func = "versions/web_static_" + tgz + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + func + "web_static")
    if not (os.path.exists(func)):
        return None
    else:
        return func
