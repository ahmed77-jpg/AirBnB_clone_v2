#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re


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

def do_deploy(archive_path):
    """ Script that does a lot of magic =) like penn and teller """
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp")
        fileonly = os.path.basename(archive_path)
        filename = os.path.splitext(fileonly)[0]
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        from_here = "/tmp/{}".format(fileonly)
        to_here = "/data/web_static/releases/{}/".format(filename)
        run("tar -xzf {} -C {}".format(from_here, to_here))
        run('rm /tmp/{}'.format(fileonly))
        run('mv {}web_static/* {}'.format(to_here, to_here))
        run('rm -rf {}web_static'.format(to_here))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(to_here))
        print('New version deployed!')
        return True
    except:
        return False
    return True
