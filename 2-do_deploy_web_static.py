#!/usr/bin/env python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.api import run, put, local, env
from datetime import datetime
import os.path
env.hosts = ['34.139.123.27', '34.73.206.129']
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
    """
    - Upload the archive to the /tmp/ directory of the web server
    - iUncompress the archive to the folder /data/web_static/releases/<archive
    filename without extension> on the web server
    - Delete the archive from the web server
    - Delete the symbolic link /data/web_static/current from the web server
    - Create a new the symbolic link /data/web_static/current on the web
    server, linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
    """
    
    if not (os.path.exists(archive_path)):
        return False
    archive_name = archive_path.split('/')[1]
    archive_name_without_ext = archive_path.split('/')[1].split('.')[0]
    release_path = '/data/web_static/releases/' + archive_name_without_ext
    upload_path = '/tmp/' + archive_name

    put(archive_path, '/tmp')
    run('sudo mkdir -p ' + release_path)
    run('sudo tar -xzf ' + upload_path + ' -C ' + release_path)
    run('sudo rm ' + upload_path)
    run('sudo mv ' + release_path + '/web_static/* ' + release_path + '/')
    run('sudo rm -rf ' + release_path + '/web_static')
    run('sudo rm -rf /data/web_static/current')
    run('sudo ln -s ' + release_path + ' /data/web_static/current')
    return True
