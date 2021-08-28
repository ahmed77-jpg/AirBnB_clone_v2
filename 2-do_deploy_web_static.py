#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local, put, run, env
import os.path

env.hosts = ["34.139.123.27", "34.73.206.129"]

def do_deploy(archive_path):
    """deploy tar package to remote server"""

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
