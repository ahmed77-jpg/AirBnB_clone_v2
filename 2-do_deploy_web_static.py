#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import run, put, local, env
from datetime import datetime
import os.path
env.hosts = ['34.73.206.129', '34.139.123.27']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not (os.path.exists(archive_path)):
        return False
    archive_name = archive_path.split('/')[1]
    archive_name_without_ext = archive_path.split('/')[1].split('.')[0]
    release_path = '/data/web_static/releases/' + archive_name_without_ext
    upload_path = '/tmp/' + archive_name
    put(archive_path, upload_path)
    run('mkdir -p ' + release_path)
    run('tar -xzf ' + upload_path + ' -C ' + release_path)
    run('rm ' + upload_path)
    run('mv ' + release_path + '/web_static/* ' + release_path + '/')
    run('rm -rf ' + release_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + release_path + ' /data/web_static/current')
    return True
